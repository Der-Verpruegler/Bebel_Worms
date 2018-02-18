import config
import numpy as np
from FIELD import field

map_width = config.RENDERAREAWIDTH
map_height = config.RENDERAREAHEIGHT
map_granularity = config.MAPGRANULARITY

class MapGenerator():
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.plain_ground()
    
    def plain_ground(self):
        """ Creates a simple map, that is horizontal and split
        half solid half permeable. """
        # Initialise the array
        array = np.empty((map_height, map_width), dtype= field.Field)
        split = map_width*(map_height/2)
        # Fill the array
        for i in range(map_height):
            for j in range(map_width):
                if i*j>split:
                    array[i,j] = field.Field(map_granularity, "AIR", [i, j])
                elif i*j<=split:
                    array[i,j] = field.Field(map_granularity, "GRASS", [i, j])
        self.array = array
        
    def hilly_ground(self):
        """ Creates a simple map, that is hilly. """
        pass
        
    def extract_solidity(self, i, j):
       solidity = self.array[i,j].solid
       return solidity
    
    def extract_colour(self, i, j):
        colour = self.array[i,j].colour
        return colour
    
    def extract_coordinates(self, i, j):
        coordinates = [self.array[i,j].x, self.array[i,j].y]
        return coordinates


class MapBackend(MapGenerator):
    """ Takes a MapGenerator object and provides specialized information."""
    def __init__(self, map):
        self.map_height = map.map_height
        self.map_width = map.map_width
        self.colours = self.get_colours(map_height, map_width)
        self.solidity = self.get_solidity(map_height, map_width) 
        self.coordinates = self.get_coordinates(map_height, map_width)
        pass
    
    def get_colours(self, map_height, map_width):
        array = np.empty((map_height, map_width), dtype= tuple)
        for i in range(map_height):
            for j in range(map_width):
                array[i,j] = map.extract_colour(i,j) 
        return array
    
    def get_solidity(self, map_height, map_width):
        array = np.empty((map_height, map_width), dtype= tuple)
        for i in range(map_height):
            for j in range(map_width):
                array[i,j] = map.extract_solidity(i,j) 
        return array
    
    def get_coordinates(self, map_height, map_width):
        array = np.empty((map_height, map_width), dtype= tuple)
        for i in range(map_height):
            for j in range(map_width):
                array[i,j] = map.extract_coordinates(i,j) 
        return array
        
    def change_map(self, i, j):
        
        def set_solidity():
            pass
        def set_colour():
            pass    
    


map = MapGenerator(map_width, map_height)
map2 = MapBackend(map)
map2.colours
map2.solidity
map2.coordinates



