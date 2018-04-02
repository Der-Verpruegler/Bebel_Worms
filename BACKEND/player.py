""""
MERELY A SKETCH OF CLAS SO FAR!
How many max players should be allowed?
Item : generic for weapon or inventory
"""
from collections import defaultdict
import math
import config
import numpy as np

from BACKEND import worm

class Player():

	def __init__(self, map, id):
		self._id = id
		self.worms = np.empty(config.NUMWORMSPERPLAYER, dtype=worm.Worm)
		for i in range(config.NUMWORMSPERPLAYER):
			self.worms[i] = worm.Worm(config.player_colours[id], map)
		self.activeWormIdx = 0
			
		self.total_health = 0

		self.items = defaultdict()
		# e.g. self.items["Prod"] = math.inf
		# e.g. self.items["Airstrike"] = 1
		# e.g. self.items["Speedup"] = 1

	def item_change(self, name, quantity, change):
		""" 
		Generic gain and use-item-function
		"""
		self.items[name] += change
		pass

	def list_items(self):
		""" 
		Generic list available items function
		"""
		return self.items

	def switch_item(self, selected):
		""" 
		Switch selected item
		"""
		self.activated_item = selected
		return

	def getActiveWorm(self):
		return self.worms[activeWormIdx]
		
	def switch_worm(self):
		self.activeWormIdx += (self.activeWormIdx + 1) % config.NUMWORMSPERPLAYER
		
	def modify_total_health(self):
		"""
		Captures aggregated health points
		"""
		# e.g. self.total_health += worm[0].health
		if self.total_health<=0:
			print("GAME OVER!")
		if self.player_name=='Frederik':
			self.total_health=0
		return

