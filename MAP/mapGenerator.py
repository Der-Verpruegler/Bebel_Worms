import config
import numpy as np

class MapGenerator:
    """ Generates an initial map and provides access functions to inherit """
    def __init__(self, colours, solidity):
        if config.GENERATIONSTYLE == "Plain ground":
            self.plain_ground(colours, solidity)
    
    def generate_field(self, row, col, terrain_type, colours, solidity):
        colours[col, row] = config.terrain_types[terrain_type]["colour"]
        solidity[col, row] = config.terrain_types[terrain_type]["solid"]
    
    def plain_ground(self, colours, solidity):
        """ Creates a simple map, that is horizontal and split
        half solid half permeable. """
        # Fill the array
        for row in range(config.RENDERAREAHEIGHT):
            for col in range(config.RENDERAREAWIDTH):
                if row < config.RENDERAREAHEIGHT / 2:
                    self.generate_field(row, col, "AIR", colours, solidity)
                else:
                    self.generate_field(row, col, "GRASS", colours, solidity)
        
    
    def hilly_ground(self):
        """ Creates a simple map, that is hilly. """
        pass


class MapBackend:
    """ Takes a MapGenerator object and provides specialized information."""
    def __init__(self):
        
        self.colours = np.empty((config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT), dtype= (int, 3))
        self.solidity = np.empty((config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT), dtype= bool)
        
        MapGenerator(self.colours, self.solidity)
     
    def px_get_solidity(self, i, j):
        """ Extracts solidity of a pixel """        
        return self.solidity[i,j]
    
    def px_get_colour(self, i, j):
        """ Extracts colour of a pixel """
        return self.colours[i,j]

    def px_set_solidity(self, i, j, boolean):
        """ Should only be used in test cases? """
        self.solidity[i,j] = boolean
        
    def px_set_colour(self, i, j, colour):
        """ Should only be used in test cases? """
        self.colours[i,j] = colour
        
    def px_set_field(self, i, j, field_type):
        """ Overwrites Field """
        self.px_set_colour(i, j, config.terrain_types[field_type]["colour"])
        self.px_set_solidity(i, j, config.terrain_types[field_type]["solid"])

