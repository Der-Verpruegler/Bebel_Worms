""""
MERELY A SKETCH OF CLAS SO FAR!
How many max players should be allowed?
Item : generic for weapon or inventory
"""
from collections import defaultdict
import math
import config


class Player():
	__TEAM_GREEN = True

	def __init__(self, map):
		if Player.__TEAM_GREEN:
			self.team = "green"
			Player.__TEAM_GREEN = False
		else:
			Player.team = "black"
			Player.__TEAM_GREEN = True

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

