import config
import json
from TERRAIN import terrain
from COORDINATES import coordinates
from SIZE import size

      
class Field(size.Size, terrain.Terrain, coordinates.Coordinates):    
    def __init__(self, square, terrain_type, koordinaten):
        size.Size.__init__(self, height=1, width=1, square=1)
        terrain.Terrain.__init__(self, terrain_type)
        coordinates.Coordinates.__init__(self, koordinaten[0], koordinaten[1])

