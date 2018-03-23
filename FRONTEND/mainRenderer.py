import config

import pygame
import numpy

class mainRenderer:
	def __init__(self):
		self._screen = pygame.display.set_mode([config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT])
		self.font = pygame.font.SysFont("monospace", 36, True)
		
	def update(self, currentTime, map, worms, activeWorm):
		self.renderMap(map)
		self.renderWorms(worms, activeWorm)
		self.renderTime(currentTime)
		pygame.display.flip()
		
	def renderTime(self, currentTime):
		if currentTime < 10:
			timeString = '00:0' + str(currentTime)[0:1]
		else:
			timeString = '00:' + str(currentTime)[0:2]
		timeLabel = self.font.render(timeString, 1, (255, 255, 255))
		self._screen.blit(timeLabel, (config.RENDERAREAWIDTH - 120, 0))
		
	def renderMap(self, map):
		pygame.surfarray.blit_array(self._screen, map)
		
	def renderWorms(self, worms, activeWorm):
		for i in range(len(worms)):
			colour = worms[i].team_colour
			if i == activeWorm:
				colour = (255, 255, 255)
			pygame.draw.rect(self._screen, colour, (worms[i].corner_col, worms[i].corner_row, worms[i].width, worms[i].height))