import config
import numpy as np
from datetime import datetime 
from FIELD import field

map_width = config.RENDERAREAWIDTH
map_height = config.RENDERAREAHEIGHT
map_granularity = config.MAPGRANULARITY

class MapGenerator():
    """ Generates an initial map and provides access functions to inherit """
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.array = self.plain_ground()
    
    
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
        return array
        
    
    def hilly_ground(self):
        """ Creates a simple map, that is hilly. """
        pass
    
        
    def px_get_solidity(self, i, j):
        """ Extracts solidity of a pixel """
        solidity = self.array[i,j].solid
        return solidity
    
    
    def px_get_colour(self, i, j):
        """ Extracts colour of a pixel """
        colour = self.array[i,j].colour
        return colour
    
    
    def px_get_coordinates(self, i, j):
        """ Extracts coordinates of a pixel, should correspond to input """
        coordinates = [self.array[i,j].x, self.array[i,j].y]
        return coordinates
    
    
    def map_get_colours(self, map_height, map_width):
        """ Provides the colours array for UI """
        array = np.empty((map_height, map_width), dtype= tuple)
        for i in range(map_height):
            for j in range(map_width):
                array[i,j] = self.px_get_colour(i,j) 
        return array
    
    
    def map_get_solidity(self, map_height, map_width):
        """ Provides the solidity array for UI """
        array = np.empty((map_height, map_width), dtype= tuple)
        for i in range(map_height):
            for j in range(map_width):
                array[i,j] = self.px_get_solidity(i,j) 
        return array
    
    
    def map_get_coordinates(self, map_height, map_width):
        """ Provides the array of coordinates """
        array = np.empty((map_height, map_width), dtype= tuple)
        for i in range(map_height):
            for j in range(map_width):
                array[i,j] = self.px_get_coordinates(i,j) 
        return array





class MapBackend(MapGenerator):
    """ Takes a MapGenerator object and provides specialized information."""
    def __init__(self, map):
        self.map_height = map.map_height
        self.map_width = map.map_width
        
        self.array = map.array
        self.colours = map.map_get_colours(self.map_height, self.map_width)
        self.solidity = map.map_get_solidity(self.map_height, self.map_width) 
        self.coordinates = map.map_get_coordinates(self.map_height, self.map_width)
        
        
    def px_get_solidity(self, i, j):
        """ Extracts solidity of a pixel """        
        return self.solidity[i,j]
    
    def px_get_colour(self, i, j):
        """ Extracts colour of a pixel """
        return self.colours[i,j]
    
    def px_get_field(self, i, j):
        """ Extracts field of a pixel """
        return self.array[i, j]


    def px_set_solidity(self, i, j, boolean):
        """ Should only be used in test cases? """
        self.solidity[i,j] = boolean

    def px_set_colour(self, i, j, colour):
        """ Should only be used in test cases? """
        self.colours[i,j] = colour
        
    def px_set_field(self, i, j, field_type):
        """ Overwrites Field """
        self.array[i,j] = field.Field(map_granularity, field_type, [i, j])
        # Update Time elapsed (hh:mm:ss.ms) 0:00:30.158059 0:00:02.344868
        #self.colours = self.map_get_colours(self.map_height, self.map_width)
        #self.solidity = self.map_get_solidity(self.map_height, self.map_width)
        # Update Time elapsed (hh:mm:ss.ms) 0:00:20.797752, 0:00:01.767589
        self.px_set_colour(i, j, field.Field(map_granularity, field_type, [i, j]).colour)
        self.px_set_solidity(i, j, field.Field(map_granularity, field_type, [i, j]).solid)
        
    
    
            
    
# Testing
start_time = datetime.now() 
map = MapGenerator(map_width, map_height)
map2 = MapBackend(map)

print(map2.px_get_colour(1,1))
print(map2.px_get_solidity(1,1))
map2.px_set_colour(1,1,"colorus")
map2.px_set_solidity(1,1,"liquidus")
print(map2.px_get_colour(1,1))
print(map2.px_get_solidity(1,1))
map2.px_set_field(1,1,"AIR")
print(map2.px_get_colour(1,1))
print(map2.px_get_solidity(1,1))

# ch if changes if set field

map2.px_set_field(1,1,"AIR")
time_elapsed = datetime.now() - start_time 
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))



