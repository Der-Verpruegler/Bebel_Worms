RENDERAREAWIDTH = 960
RENDERAREAHEIGHT = 540
MAPGRANULARITY = 1 # in px
PIXELSCALINGFACTOR = 2

WORM_WIDTH = 12
WORM_HEIGHT = 25
WORM_VERT_GAIN = 4
WORM_JUMP_HEIGHT = 20

NUMWORMSPERPLAYER = 4
NUMPLAYERS = 2

TIMEPERROUND = 60

ITERATIONSPERSECOND = 60

GENERATIONSTYLE = "Dev Test"
#GENERATIONSTYLE = "North Country"
#GENERATIONSTYLE = "Proving Grounds"

terrain_types = {
"GRASS": [{"colour": [110, 163, 20], "solid":True}],

"DARKGRASS": [{"colour": [102, 143, 0], "solid":True}],

"AIR": [{"colour": [115, 127, 255], "solid": False},
{"colour": [120, 135, 245], "solid": False},
{"colour": [123, 127, 250], "solid": False}],

"SOIL": [{"colour": [128, 43, 0], "solid": True},
{"colour": [126, 41, 0], "solid": True},
{"colour": [124, 46, 0], "solid": True},
{"colour": [131, 37, 0], "solid": True},
{"colour": [125, 35, 0], "solid": True},
{"colour": [120, 50, 0], "solid": True}],

"EARTHCORE": [{"colour": [115, 41, 0], "solid": True},
{"colour": [112, 31, 0], "solid": True},
{"colour": [115, 21, 0], "solid": True},
{"colour": [109, 37, 0], "solid": True}],

"CLOUD": [{"colour": [220, 220, 255], "solid": False}]
}

SHARE_EARTHCORE = 0.02

player_colours = [(0, 0, 0), (0, 255, 0)]