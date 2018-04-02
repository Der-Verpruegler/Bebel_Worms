import config

import pygame
import numpy

class mainRenderer:
	def __init__(self):
		self._screen = pygame.display.set_mode([config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT])
		
	def update(self, map, players):
		self.renderMap(map)
		self.renderWorms(players)
		pygame.display.flip()
		
	def renderMap(self, map):
		pygame.surfarray.blit_array(self._screen, map)
		
	def renderWorms(self, players):
		for player in players:
			for worm in player.worms:
				pygame.draw.rect(self._screen, worm._colour, (worm.corner_col, worm.corner_row, worm.width, worm.height))