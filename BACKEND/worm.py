import time
import numpy as np
import config


class Worm():
	__TEAM_GREEN = True
	def __init__(self, map):
		self.width = config.WORM_WIDTH
		self.height = config.WORM_HEIGHT
		self.map = map
		if Worm.__TEAM_GREEN:
			self.team = "green"
			self.team_colour = config.worm_types["WORM_GREEN"]["colour"]
			Worm.__TEAM_GREEN = False
		else:
			self.team = "black"
			self.team_colour = config.worm_types["WORM_BLACK"]["colour"]
			Worm.__TEAM_GREEN = True
		self.spawn()


	def spawn(self):
		""" Find a random valid spawn point on map """
		valid_spawn = False
		while valid_spawn is False:
			# A random column on map
			guess = np.random.randint(0, config.RENDERAREAWIDTH-self.width)
			# Get hitbox coords
			collision = self.wrap_hitbox_collision(col=guess, row=0)
			# Check if there is collision with map in shitbox
			# If not => valid spawn, otherwise try different rand
			if not collision:
				valid_spawn = True
				# Instance vars describing the pos
				self.corner_col = guess
				self.corner_row = 0
				# Dirty map hacking? Alternatives to be discussed!
				self.update_map(self.get_hitbox(self.corner_col, self.corner_row), True)
		return self.corner_col, self.corner_row


	def update_map(self, box, how):
		self.map.solidity[box[0][0]:box[1][0], box[0][1]:box[1][1]] = how


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

		# efficient boxing
		sub_map = self.map.solidity[box[0][0]:box[1][0], box[0][1]:box[1][1]]
		return sub_map.any()


	def wrap_hitbox_collision(self, col, row):
		hitbox = self.get_hitbox(col, row)
		return self.check_for_box_collision(hitbox)


	def move(self, direction, speed=1):
		""" All movements of worm """

		def horizontal_move(speed):
			""" Generic function for horizontal moves """

			# For speed ups: #TODO: MAKE THIS WORK!
			# if np.abs(speed)>1: 
			# 	print("yoyo")
			# 	# Make current hitbox "invisible", important for collision detection
			# 	self.update_map(self.get_hitbox(self.corner_col, self.corner_row), False)
			# 	has_ground_below = self.wrap_hitbox_collision(col=self.corner_col, row=self.corner_row+1)
			# 	move_step = 0
			# 	while move_step<=abs(speed):
			# 		print("heyhey")
			# 		collision = self.wrap_hitbox_collision(col=self.corner_col+move_step, row=self.corner_row)
			# 		if collision and has_ground_below:
			# 			self.corner_col += move_step
			# 			print("here")
			# 			break
			# 		else:
			# 			move_step += 1	
			# 	self.update_map(self.get_hitbox(self.corner_col, self.corner_row), True)
			# Standard speed:
			#else:
			j = 0
			while j < config.WORM_VERT_GAIN:
				# Make current hitbox "invisible", important for collision detection
				self.update_map(self.get_hitbox(self.corner_col, self.corner_row), False)
				has_ground_below = self.wrap_hitbox_collision(col=self.corner_col, row=self.corner_row+1)
				collision = self.wrap_hitbox_collision(col=self.corner_col+speed, row=self.corner_row-j)					
				if has_ground_below and not collision:
					self.corner_col += speed
					self.corner_row -= j
					# If uphill: slow worm!
					time.sleep(j/10)
					break
				j += 1
			# Whatever the endposition is, make it solid
			self.update_map(self.get_hitbox(self.corner_col, self.corner_row), True)


		if direction == "left" and not self.corner_col-1 < 0:
			horizontal_move(-1) # TODO: get rid of default value!


		elif direction == "right" and not self.corner_col+1 > (config.RENDERAREAWIDTH-config.WORM_WIDTH):
			horizontal_move(1) # TODO: get rid of default value!


		elif direction == "up":
			# Make current hitbox "invisible", important for collision detection
			self.update_map(self.get_hitbox(self.corner_col, self.corner_row), False)
			has_ground_below = self.wrap_hitbox_collision(self.corner_col, self.corner_row + 1)
			if has_ground_below:
				j = 0
				while j < config.WORM_JUMP_HEIGHT:
					k = max(1, j)
					collision = self.wrap_hitbox_collision(col=self.corner_col, row=self.corner_row-k)
					if collision:
						break
					self.corner_row -= 1
					self.update_map(self.get_hitbox(self.corner_col, self.corner_row), False)
					j += 1
			# Whatever the endposition is, make it solid
			self.update_map(self.get_hitbox(self.corner_col, self.corner_row), True)


		elif direction == "down":
			# Make current hitbox "invisible", important for collision detection
			self.update_map(self.get_hitbox(self.corner_col, self.corner_row), False)
			collision = self.wrap_hitbox_collision(self.corner_col, self.corner_row + 1)
			if not collision:
				self.corner_row += 1
			# Whatever the endposition is, make it solid
			self.update_map(self.get_hitbox(self.corner_col, self.corner_row), True)
