RENDERAREAWIDTH = 960
RENDERAREAHEIGHT = 540
MAPGRANULARITY = 1 # in px
PIXELSCALINGFACTOR = 2

WORM_WIDTH = 12
WORM_HEIGHT = 25
WORM_VERT_GAIN = 4
WORM_JUMP_HEIGHT = 20
NUMWORMS = 8

ITERATIONSPERSECOND = 60

GENERATIONSTYLE = "Mystic Peaks"

terrain_types = {
"GRASS": {"colour": [110, 163, 20], "solid":True},
"DARKGRASS": {"colour": [102, 143, 0], "solid":True},
"AIR1": {"colour": [115, 127, 255], "solid": False},
"AIR2": {"colour": [120, 135, 245], "solid": False},
"AIR3": {"colour": [123, 127, 250], "solid": False},
"SOIL1": {"colour": [128, 43, 0], "solid": True},
"SOIL2": {"colour": [126, 41, 0], "solid": True},
"SOIL3": {"colour": [124, 46, 0], "solid": True},
"SOIL4": {"colour": [131, 37, 0], "solid": True},
"SOIL5": {"colour": [125, 35, 0], "solid": True},
"SOIL6": {"colour": [120, 50, 0], "solid": True},
"EARTHCORE1": {"colour": [115, 41, 0], "solid": True},
"EARTHCORE2": {"colour": [112, 31, 0], "solid": True},
"EARTHCORE3": {"colour": [115, 21, 0], "solid": True},
"EARTHCORE4": {"colour": [109, 37, 0], "solid": True},
"CLOUD": {"colour": [220, 220, 255], "solid": False}
}

worm_types = {
"WORM_BLACK": {"colour": [20, 20, 55], "solid": True},
"WORM_GREEN": {"colour": [251, 204, 231], "solid": True}
}

VAR_AIR = 3
VAR_SOIL = 6
VAR_EARTHCORE = 4

