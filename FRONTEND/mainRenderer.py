import config

import pygame
import numpy

class mainRenderer:
	def __init__(self):
		self._screen = pygame.display.set_mode([config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT])
		self.font = pygame.font.SysFont("monospace", 36, True)
		
	def update(self, currentTime, map, players, activePlayer):
		self.renderMap(map)
		self.renderWorms(players, activePlayer)
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
		
	def renderWorms(self, players, activePlayer):
		for i in range(len(players)):
			for j in range(len(players[i].worms)):
				colour = (255, 255, 255) if (i == activePlayer and j == players[i].activeWormIdx) else players[i].worms[j]._colour
				pygame.draw.rect(self._screen, colour, (players[i].worms[j].corner_col, players[i].worms[j].corner_row, players[i].worms[j].width, players[i].worms[j].height))
