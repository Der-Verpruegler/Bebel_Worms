# pylint: disable=W0312, E1101
import numpy as np
import config


class Worm():
	def __init__(self, team_colour, map):
		self.width = config.WORM_WIDTH
		self.height = config.WORM_HEIGHT
		self.map = map
		self._team_colour = team_colour
		self.health = config.WORM_HEALTH
		self.spawn()

	def spawn(self):
		""" Find a random valid spawn point on map """
		valid_spawn = False
		while valid_spawn is False:
			# A random column on map
			guess = np.random.randint(0, config.RENDERAREAWIDTH-self.width)
			# Get hitbox coords
			collision = self.eval_hitbox_collision(col=guess, row=0)
			# Check if there is collision with map in shitbox
			# If not => valid spawn, otherwise try different rand
			if not collision:
				valid_spawn = True
				# Instance vars describing the pos
				self.corner_col = guess
				self.corner_row = 0
				self.wrap_set_map_solidity(self.corner_col, self.corner_row, True)
		return self.corner_col, self.corner_row


	def get_hitbox(self, col, row):
		"""
		Get worm hitbox from col/row, which is a rectangle.
		Is input to def check_for_box_collision
		"""
		p1 = [col, row] # upper left
		p2 = [col + self.width, row + self.height] # lower right
		return [p1, p2]


	def check_for_box_collision(self, box):
		"""
		Checks if hitbox touches solid pixel
		True if there is a collision, False if not
		Throws exception message if out of map, should be avoided
		"""
		if box[0][0] < 0:
			raise Exception("Out of Map, box[0][0]:" + str(box[0][0]))
		if box[1][0] > config.RENDERAREAWIDTH:
			raise Exception("Out of Map, box[1][0]:" + str(box[1][0]))
		sub_map = self.map.box_get_solidity(box)
		return sub_map.any()


	def eval_hitbox_collision(self, col, row):
		"""
		A wrapper to save lines of code
		Checks a hitbox for collision.
		"""
		box = self.get_hitbox(col, row)
		return self.check_for_box_collision(box)


	def wrap_set_map_solidity(self, col, row, boolean):
		"""
		A wrapper to save lines of code
		Modifies the solidity-array by a box.
		"""
		box = self.get_hitbox(col, row)
		self.map.box_set_solidity(box, boolean)

	def move(self, direction):
		"""
		Args: "left", "right", "up"
		"""
		mapping = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0,1]}
		self.wrap_set_map_solidity(self.corner_col, self.corner_row, False)
		collision = self.eval_hitbox_collision(self.corner_col + mapping[direction][1], self.corner_row + mapping[direction][0])
		if not collision:
			self.corner_col += mapping[direction][1]
			self.corner_row += mapping[direction][0]
		self.wrap_set_map_solidity(self.corner_col, self.corner_row, True)
		return self.eval_hitbox_collision(self.corner_col, self.corner_row + 1)
