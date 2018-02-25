import json

class Terrain():
    def __init__(self, terrain_type):
        i = False
        if i: # 0:01:12.544400
            def parse_input(input_file):
                with open(input_file) as json_data:
                    return json.load(json_data)

            terrain_data = parse_input("./terrain.json")
        else: #0:00:02.662865
            terrain_data = {
                            "grass": {"colour": (127, 255, 127), "solid":True},
                            "sky": {"colour": (127, 127, 255), "solid": False},
                            "air": {"colour": (127, 127, 255), "solid": False},
                            "cloud": {"colour": (220, 220, 255), "solid": False}
                            }

        terrain_type = terrain_type.lower()

        self.solid = terrain_data[terrain_type]['solid']
        self.colour = terrain_data[terrain_type]['colour']
