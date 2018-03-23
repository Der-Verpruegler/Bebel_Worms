# pylint: disable=maybe-no-member
import numpy as np
import time
import config


class MapGenerator:
    """ Generates an initial map """
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
        
    def generate_mult_field(self, col, split, choice, colours, solidity):
        """ Generates multiple fields at once, optimization """
        colours[col, 0:split] = [config.terrain_types[terrain_type]["colour"] for terrain_type in choice] 
        solidity[col, 0:split] = [config.terrain_types[terrain_type]["solid"] for terrain_type in choice]      

    def field_filler(self, process, colours, solidity):
        """ Fills the map with fields, regarding the solidity split
            pattern (process) and adds random jitter """

        for col in range(config.RENDERAREAWIDTH):
            split = process[col]
            choice = np.random.choice(["AIR" + str(i) for i in range(1, config.VAR_AIR)], split)
            self.generate_mult_field(col, split, choice, colours, solidity)
            for row in range(split, config.RENDERAREAHEIGHT):
                if (row - np.random.randint(5, 10)) < split:
                    choice = "GRASS"
                elif (row - np.random.randint(18, 20)) < split:
                    choice = "DARKGRASS"
                elif (config.RENDERAREAHEIGHT - np.random.randint(10, np.random.randint(30, 60))) > row:
                    choice = np.random.choice(["SOIL" + str(i) for i in range(1, config.VAR_SOIL)])
                else:
                    choice = np.random.choice(["EARTHCORE" + str(i) for i in range(1, config.VAR_EARTHCORE)])
                self.generate_field(col, row, choice, colours, solidity)

    def style_proving_grounds(self, colours, solidity):
        """ Creates a simple map, that is horizontal and split
        half solid half permeable. """
        # Fill the array
        process = np.full((config.RENDERAREAWIDTH), config.RENDERAREAHEIGHT / 2)
        start = time.clock()
        print("Start: ", start)
        last_step = time.clock()
        self.field_filler(process, colours, solidity)
        print("Field-Filler: ", time.clock() - last_step)

    def style_north_country(self, colours, solidity):
        """ Creates a simple map, that is hilly. """
        process = np.random.randint(0, config.RENDERAREAHEIGHT, config.RENDERAREAWIDTH)
        start = time.clock()
        print("Start: ", start)
        process = self.smoother(process, 2)
        print("Smoother: ", time.clock()- start)
        process = self.blocker(process, 12)
        print("Blocker: ", time.clock()- start)
        process = self.smoother(process, 17)
        print("Smoother: ", time.clock()- start)
        last_step = time.clock()
        self.field_filler(process, colours, solidity)
        print("Field-Filler: ", time.clock() - last_step)


    def style_mystic_peaks(self, colours, solidity):
        """ Creates a mystical map, that has steepness. """
        process = np.random.randint(0, config.RENDERAREAHEIGHT, config.RENDERAREAWIDTH)
        start = time.clock()
        print("Start: ", start)        
        process = self.extremizer(process, 5)
        print("Extremizer: ", time.clock()- start)
        process = self.smoother(process, 5)
        print("Smoother: ", time.clock()- start)
        process = self.blocker(process, 15)
        print("Blocker: ", time.clock()- start)
        process = self.smoother(process, 15)
        print("Smoother: ", time.clock()- start)
        last_step = time.clock()
        self.field_filler(process, colours, solidity)
        print("Field-Filler: ", time.clock() - last_step)

    def extremizer(self, process, window):
        """ Extremizes by either min/max-ing in window"""
        chunks = int(config.RENDERAREAWIDTH/window)
        split = np.linspace(0, config.RENDERAREAWIDTH, chunks).astype(int)
        for i in range(len(split)-1):
            sub_ = process[int(split[i]):int(split[i+1])]
            if np.random.randint(0, 2) == 1:
                process[split[i]:split[i+1]] = np.max(sub_)
            else:
                process[split[i]:split[i+1]] = np.min(sub_)
        return process


    def smoother(self, process, window):
        """ Smoothes by averaging in window"""
        proc_leng = len(process)
        for i in range(proc_leng):
            if i > (proc_leng - window):
                process[i] = np.average(process[i-window:proc_leng])
            elif i < window:
                process[i] = np.average(process[0:i+window])
            else:
                process[i] = np.average(process[i-window:i+window])
        return process


    def blocker(self, process, window):
        """ Evens ground out by proceeding in blocks """
        chunks = int(config.RENDERAREAWIDTH/window)
        split = np.linspace(0, config.RENDERAREAWIDTH, chunks).astype(int)
        for i in range(len(split)-1):
            sub_ = process[int(split[i]):int(split[i+1])]
            if np.random.randint(0, 2) == 1:
                process[int(split[i]):int(split[i+1])] = np.average(sub_)
            else:
                process[int(split[i]):int(split[i+1])] = np.median(sub_)
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
