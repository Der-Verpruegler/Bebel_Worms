# pylint: disable=W0312, E1101
import time
import numpy as np
import config


class MapGenerator:
	""" Generates an initial map """
	def __init__(self, colours, solidity):
		if config.GENERATIONSTYLE == "Proving Grounds":
			self.style_proving_grounds(colours, solidity)
		if config.GENERATIONSTYLE == "North Country":
			self.style_north_country(colours, solidity)
		if config.GENERATIONSTYLE == "Mystic Peaks":
			self.style_mystic_peaks(colours, solidity)
		if config.GENERATIONSTYLE == "Dev Test":
			self.style_dev_test(colours, solidity)			

	def generate_field(self, col, row, terrain_type, colours, solidity):
		"""
		Generates a field for a specific coordinate.
		col = x-axis
		row = y-axis
		terrain_type = dictionary entry
		colours, solidity = arrays keeping track of map structure
		"""
		colours[col, row] = terrain_type["colour"]
		solidity[col, row] = terrain_type["solid"]

	def generate_mult_field(self, col, row_start, row_end, choice, colours, solidity):
		""" 
		Generates multiple fields at once, faster than generate_field()
		So far: still per column.
		"""
		colours[col, row_start:row_end] = [terrain_type["colour"] for terrain_type in choice]
		solidity[col, row_start:row_end] = [terrain_type["solid"] for terrain_type in choice]

	def field_filler(self, process, colours, solidity):
		"""
		Fills the map with fields, regarding the split
		pattern (process) defined by solidity and adds random jitter
		in the overlap areas.
		"""
		# Abbreviate vars for shorter lines
		MAP_HEIGHT = config.RENDERAREAHEIGHT
		SH_CORE = int(config.SHARE_EARTHCORE * MAP_HEIGHT)

		for col in range(config.RENDERAREAWIDTH):
			# Save time I (Air is filled up until split)
			split = process[col]
			terrain_type = np.random.choice(config.terrain_types["AIR"], split)
			self.generate_mult_field(col, 0, split, terrain_type, colours, solidity)

			# Save time II (Earth is filled up from below)
			terrain_type = np.random.choice(config.terrain_types["EARTHCORE"], 10)
			self.generate_mult_field(col, MAP_HEIGHT - SH_CORE, MAP_HEIGHT, terrain_type, colours, solidity)

			# Random filling rest, hard to optimize
			for row in range(split, MAP_HEIGHT - SH_CORE):
				if row < split + np.random.randint(5, 10):
					terrain_type = np.random.choice(config.terrain_types["GRASS"])
				elif row < split + np.random.randint(18, 20):
					terrain_type = np.random.choice(config.terrain_types["DARKGRASS"])
				elif row < (MAP_HEIGHT - np.random.randint(SH_CORE, np.random.randint(30, 60))):
					terrain_type = np.random.choice(config.terrain_types["SOIL"])
				else:
					terrain_type = np.random.choice(config.terrain_types["EARTHCORE"])
				#print(terrain_type)
				self.generate_field(col, row, terrain_type, colours, solidity)

	def create_caves(self, where):
		""" Template function to add caves into map (subsequent) """
		pass

	def style_dev_test(self, colours, solidity):
		"""
		Optimized Map - simply for dev purposes
		"""
		def mass_fill(terrain, property, half_map, width):
			return [[terrain[property] for row in range(half_map)] for col in range(width)]

		start = time.clock()		
		MAP_HEIGHT = config.RENDERAREAHEIGHT
		MAP_WIDTH = config.RENDERAREAWIDTH
		half_map = int(MAP_HEIGHT/2)
		colours[0:MAP_WIDTH, 0:half_map] = mass_fill(config.terrain_types["AIR"][0], 'colour', half_map, MAP_WIDTH)
		solidity[0:MAP_WIDTH, 0:half_map] = mass_fill(config.terrain_types["AIR"][0], 'solid', half_map, MAP_WIDTH)
		colours[0:MAP_WIDTH, half_map:MAP_HEIGHT] = mass_fill(config.terrain_types["GRASS"][0], 'colour', half_map, MAP_WIDTH)
		solidity[0:MAP_WIDTH, half_map:MAP_HEIGHT] = mass_fill(config.terrain_types["GRASS"][0], 'solid', half_map, MAP_WIDTH)
		print("Total time: ", time.clock() - start)

	def style_proving_grounds(self, colours, solidity):
		"""
		Creates a simple map, that is horizontal and split
		half solid half permeable. 
		Out: Process, int-array indicating per column 
		in which row the solid/non-solid split is.
		"""
		# Fill the array
		start = time.clock()
		process = np.full((config.RENDERAREAWIDTH), np.int(config.RENDERAREAHEIGHT / 2))
		last_step = time.clock()
		self.field_filler(process, colours, solidity)
		print("Total time: ", time.clock() - start)

	def style_north_country(self, colours, solidity):
		"""
		Creates a simple map, that is hilly. 
		Out: Process, int-array indicating per column 
		in which row the solid/non-solid split is.
		"""
		start = time.clock()
		process = np.random.randint(0, config.RENDERAREAHEIGHT, config.RENDERAREAWIDTH)		
		process = self.smoother(process, 2)
		process = self.blocker(process, 12)
		process = self.smoother(process, 17)
		self.field_filler(process, colours, solidity)
		print("Total time: ", time.clock() - start)


	def style_mystic_peaks(self, colours, solidity):
		"""
		Creates a mystical map, that has considerable steepness.
		Out: Process, int-array indicating per column
		in which row the solid/non-solid split is.
		"""
		start = time.clock()
		process = np.random.randint(0, config.RENDERAREAHEIGHT, config.RENDERAREAWIDTH)		
		process = self.extremizer(process, 8)
		process = self.smoother(process, 5)
		process = self.blocker(process, 15)
		process = self.smoother(process, 15)
		self.field_filler(process, colours, solidity)
		print("Total time: ", time.clock() - start)

	def extremizer(self, process, window):
		""" Extremizes by either min/max-ing in window"""
		chunks = int(config.RENDERAREAWIDTH/window)
		split = np.linspace(0, config.RENDERAREAWIDTH, chunks).astype(int)
		for i in range(len(split)-1):
			sub_ = process[int(split[i]):int(split[i+1])]
			if np.random.randint(0, 2) == 1:
				process[split[i]:split[i+1]] = np.max(sub_)
			else:
				process[split[i]:split[i+1]] = np.min(sub_)
		return process


	def smoother(self, process, window):
		""" Smoothes by averaging in window"""
		proc_leng = len(process)
		for i in range(proc_leng):
			if i > (proc_leng - window):
				process[i] = np.average(process[i-window:proc_leng])
			elif i < window:
				process[i] = np.average(process[0:i+window])
			else:
				process[i] = np.average(process[i-window:i+window])
		return process


	def blocker(self, process, window):
		""" Evens ground out by proceeding in blocks """
		chunks = int(config.RENDERAREAWIDTH/window)
		split = np.linspace(0, config.RENDERAREAWIDTH, chunks).astype(int)
		for i in range(len(split)-1):
			sub_ = process[int(split[i]):int(split[i+1])]
			if np.random.randint(0, 2) == 1:
				process[int(split[i]):int(split[i+1])] = np.average(sub_)
			else:
				process[int(split[i]):int(split[i+1])] = np.median(sub_)
		return process


class MapBackend:
	""" Takes a MapGenerator object and provides specialized information."""
	def __init__(self):

		self.colours = np.empty((config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT), dtype=(int, 3))
		self.solidity = np.empty((config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT), dtype=bool)

		MapGenerator(self.colours, self.solidity)

	def px_get_solidity(self, col, row):
		""" Extracts solidity of a pixel """
		return self.solidity[col, row]

	def box_get_solidity(self, box):
		""" Returns the solidity in a geometric rectangle, defined by box """
		return self.solidity[box[0][0]:box[1][0], box[0][1]:box[1][1]]

	def px_get_colour(self, col, row):
		""" Extracts colour of a pixel """
		return self.colours[col, row]

	def px_set_solidity(self, col, row, boolean):
		""" Should only be used in test cases? """
		self.solidity[col, row] = boolean

	def box_set_solidity(self, box, boolean):
		""" Changes the solidity in a geometric rectangle, defined by box """
		self.solidity[box[0][0]:box[1][0], box[0][1]:box[1][1]] = boolean

	def px_set_colour(self, col, row, colour):
		""" Should only be used in test cases? """
		self.colours[col, row] = colour

	def px_set_field(self, col, row, field_type):
		""" Overwrites Field """
		self.px_set_colour(col, row, config.terrain_types[field_type]["colour"])
		self.px_set_solidity(col, row, config.terrain_types[field_type]["solid"])
