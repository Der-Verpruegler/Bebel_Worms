import config

import numpy

class mainRenderer:
	def __init__(self, pygame):
		self._pygame = pygame
		self._screen = self._pygame.display.set_mode([config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT])
		
	def update(self, map, worms):
		self.renderMap(map)
		self.renderWorms(worms)
		self._pygame.display.flip()
		
	def renderMap(self, map):
		self._pygame.surfarray.blit_array(self._screen, map)
		
	def renderWorms(self, worms):
		for worm in worms:
			self._pygame.draw.rect(self._screen, worm.team_colour, (worm.corner_col, worm.corner_row, worm.width, worm.height))