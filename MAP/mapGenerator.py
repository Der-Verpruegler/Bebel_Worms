import config
import numpy as np
from FIELD import field

map_width = config.RENDERAREAWIDTH
map_height = config.RENDERAREAHEIGHT

class MapGenerator():
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.plain_ground()
    
    def plain_ground(self):
        # Initialise the array
        array = np.empty([map_height, map_width], dtype=object)
        split = map_width*(map_height/2)
        # Fill the array
        for i in range(map_height):
            for j in range(map_width):
                if i*j>split:
                    array[i,j] = field.Field(1, "AIR", [i, j])
                elif i*j<=split:
                    array[i,j] = field.Field(1, "GRASS", [i, j])
        self.array = array
        
    def extract_terrain(self, i, j):
        self.terrain = self.array[i,j].terrain_type
        
        
        
        

map = MapGenerator(map_width, map_height)
map.extract_terrain(0,1)



