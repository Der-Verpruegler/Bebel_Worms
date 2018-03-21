from collections import defaultdict
import math
#import config


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

		self.weapons = defaultdict()
		# e.g. self.weapons["Prod"] = math.inf
		# e.g. self.weapons["Airstrike"] = 1

		self.inventory = defaultdict()
		# eg. self.inventory["Speedup"] = 1

	def gain_item(self, boost_item, name, quantity):
		""" 
		Item := Weapon or Boost 
		Generic gain-item-function
		"""
		# e.g. self.boost_item[name] += quantity
		pass

	def list_items(self):
		""" 
		Item := Weapon or Boost 
		Generic list-item-function
		"""
		pass

	def switch_item(self, selected):
		""" 
		Item := Weapon or Boost 
		Switch selected item
		"""
		pass

	def modify_total_health(self):
		"""
		Captures aggregated health points
		"""
		# e.g. self.total_health += worm[0].health
		if self.total_health<=0:
			print("GAME OVER!")		


