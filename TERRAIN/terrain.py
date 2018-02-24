import json

class Terrain():
    def __init__(self, terrain_type):

        def parse_input(input_file):
            with open(input_file) as json_data:
                return json.load(json_data)

        terrain_data = parse_input("./terrain.json")
        terrain_type = terrain_type.lower()

        self.solid = terrain_data[terrain_type]['solid']
        self.colour = terrain_data[terrain_type]['colour']
