import config

class Terrain():
    # To Do: Auslagern des Krams in Config
    def __init__(self, terrain_type):
        if terrain_type in ['GRASS', 'STONE', 'ROCK']:
            self.solid = True
        if terrain_type in ['WATER', 'AIR', 'CLOUD']:
            self.solid = False
        if terrain_type == 'GRASS':
            self.colour = (127, 255, 127)
        if terrain_type == 'AIR':
            self.colour = (127, 127, 255)
    

class Size:
    def __init__(self, height=1, width=1, square=1):
        self.height = height
        self.width = width
        self.square = square
        
        
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Field(Size, Terrain, Coordinates):
    
    def __init__(self, square, terrain_type, coordinates):
        Size.__init__(self, height=1 , width=1 , square=1)
        Terrain.__init__(self, terrain_type)
        Coordinates.__init__(self, coordinates[0], coordinates[1])

        
        
    