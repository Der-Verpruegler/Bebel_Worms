# pylint: disable=maybe-no-member
import numpy as np
import config


class MapGenerator:
    """ Generates an initial map and provides access functions to inherit """
    def __init__(self, colours, solidity):
        if config.GENERATIONSTYLE == "Plain ground":
            self.hilly_ground(colours, solidity)

    def generate_field(self, col, row, terrain_type, colours, solidity):
        colours[col, row] = config.terrain_types[terrain_type]["colour"]
        solidity[col, row] = config.terrain_types[terrain_type]["solid"]


    def plain_ground(self, colours, solidity):
        """ Creates a simple map, that is horizontal and split
        half solid half permeable. """
        # Fill the array
        for row in range(config.RENDERAREAHEIGHT):
            for col in range(config.RENDERAREAWIDTH):
                if row < config.RENDERAREAHEIGHT / 2:
                    self.generate_field(col, row, "AIR", colours, solidity)
                else:
                    self.generate_field(col, row, "GRASS", colours, solidity)


    def hilly_ground(self, colours, solidity):
        """ Creates a simple map, that is hilly. """
        process = np.random.randint(0, config.RENDERAREAHEIGHT, config.RENDERAREAWIDTH)
        process = self.smoother(process, 2)
        process = self.blocker(process, 10)
        process = self.smoother(process, 10)
        for col in range(config.RENDERAREAWIDTH):
            split = process[col]
            for row in range(config.RENDERAREAHEIGHT):
                if row < split:
                    self.generate_field(col, row, "AIR", colours, solidity)
                else:
                    self.generate_field(col, row, "GRASS", colours, solidity)


    def smoother(self, process, window):
        """ Smoothes by averaging in window"""
        for i in range(len(process)):
            if i > (len(process) - window):
                process[i] = np.average(process[i-window:i])
            if i < window:
                process[i] = np.average(process[i:i+window])
            else:
                process[i] = np.average(process[i-window:i+window])
        return process


    def blocker(self, process, window):
        """ Evens ground out by proceeding in blocks """
        chunks = int(config.RENDERAREAWIDTH/window)
        split = np.linspace(0, config.RENDERAREAWIDTH, chunks).astype(int)
        for i in range(len(split)-1):
            if np.random.randint(0, 2) == 1:
                local_average = np.average(process[int(split[i]):int(split[i+1])])
                process[int(split[i]):int(split[i+1])] = local_average
            else:
                local_median = np.median(process[int(split[i]):int(split[i+1])])
                process[int(split[i]):int(split[i+1])] = local_median
        return process


class MapBackend:
    """ Takes a MapGenerator object and provides specialized information."""
    def __init__(self):

        self.colours = np.empty((config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT), dtype=(int, 3))
        self.solidity = np.empty((config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT), dtype=bool)

        MapGenerator(self.colours, self.solidity)

    def px_get_solidity(self, col, row):
        """ Extracts solidity of a pixel """
        return self.solidity[col, row]

    def px_get_colour(self, col, row):
        """ Extracts colour of a pixel """
        return self.colours[col, row]

    def px_set_solidity(self, col, row, boolean):
        """ Should only be used in test cases? """
        self.solidity[col, row] = boolean

    def px_set_colour(self, col, row, colour):
        """ Should only be used in test cases? """
        self.colours[col, row] = colour

    def px_set_field(self, col, row, field_type):
        """ Overwrites Field """
        self.px_set_colour(col, row, config.terrain_types[field_type]["colour"])
        self.px_set_solidity(col, row, config.terrain_types[field_type]["solid"])
