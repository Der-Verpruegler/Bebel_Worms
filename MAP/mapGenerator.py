# pylint: disable=maybe-no-member
import numpy as np
import config


class MapGenerator:
    """ Generates an initial map and provides access functions to inherit """
    def __init__(self, colours, solidity):
        if config.GENERATIONSTYLE == "Proving Grounds":
            self.style_proving_grounds(colours, solidity)
        if config.GENERATIONSTYLE == "North Country":
            self.style_north_country(colours, solidity)
        if config.GENERATIONSTYLE == "Mystic Peaks":
            self.style_mystic_peaks(colours, solidity)            

    def generate_field(self, col, row, terrain_type, colours, solidity):
        colours[col, row] = config.terrain_types[terrain_type]["colour"]
        solidity[col, row] = config.terrain_types[terrain_type]["solid"]


    def field_filler(self, process_chain, colours, solidity):
        for col in range(config.RENDERAREAWIDTH):
            split = process_chain[col]
            for row in range(config.RENDERAREAHEIGHT):
                
                if row < split:
                    choices = ["AIR1", "AIR2", "AIR3"]
                    choice = np.random.choice(choices)
                    self.generate_field(col, row, choice, colours, solidity)
                    
                elif (row - np.random.randint(5, 10)) < split:
                    self.generate_field(col, row, "GRASS", colours, solidity)
                    
                elif (row - np.random.randint(18, 20)) < split:
                    self.generate_field(col, row, "DARKGRASS", colours, solidity)
                    
                elif (config.RENDERAREAHEIGHT - np.random.randint(10, np.random.randint(30, 60))) > row:
                    choices = ["SOIL1", "SOIL2", "SOIL3", "SOIL4", "SOIL5", "SOIL6"]
                    choice = np.random.choice(choices)
                    self.generate_field(col, row, choice, colours, solidity)
                    
                else:
                    choices = ["EARTHCORE1", "EARTHCORE2", "EARTHCORE3", "EARTHCORE4"]
                    choice = np.random.choice(choices)
                    self.generate_field(col, row, choice, colours, solidity)                    


    def style_proving_grounds(self, colours, solidity):
        """ Creates a simple map, that is horizontal and split
        half solid half permeable. """
        # Fill the array
        process = np.full((config.RENDERAREAWIDTH), config.RENDERAREAHEIGHT / 2)
        self.field_filler(process, colours, solidity)


    def style_north_country(self, colours, solidity):
        """ Creates a simple map, that is hilly. """
        process = np.random.randint(0, config.RENDERAREAHEIGHT, config.RENDERAREAWIDTH)
        process = self.smoother(process, 2)
        process = self.blocker(process, 12)
        process = self.smoother(process, 17)    
        self.field_filler(process, colours, solidity)
     
               
    def style_mystic_peaks(self, colours, solidity):
        """ Creates a mystical map, that has steepness. """
        process = np.random.randint(0, config.RENDERAREAHEIGHT, config.RENDERAREAWIDTH)
        process = self.extremizer(process, 5)
        process = self.smoother(process, 5)
        process = self.blocker(process, 15)
        process = self.smoother(process, 15)        
        self.field_filler(process, colours, solidity) 


    def extremizer(self, process, window):
        """ Extremizes by either min/max-ing in window"""
        chunks = int(config.RENDERAREAWIDTH/window)
        split = np.linspace(0, config.RENDERAREAWIDTH, chunks).astype(int)
        for i in range(len(split)-1):
            if np.random.randint(0, 2) == 1:
                local_average = np.max(process[int(split[i]):int(split[i+1])])
                process[int(split[i]):int(split[i+1])] = local_average
            else:
                local_median = np.min(process[int(split[i]):int(split[i+1])])
                process[int(split[i]):int(split[i+1])] = local_median
        return process


    def smoother(self, process, window):
        """ Smoothes by averaging in window"""
        for i in range(len(process)):
            if i > (len(process) - window):
                process[i] = np.average(process[i-window:i])
            if i < window:
                process[i] = np.average(process[0:i+window])
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
