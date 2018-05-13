# pylint: disable=W0312, E1101
import time
import pygame

import config


class mainRenderer:
	def __init__(self):
		self._screen = pygame.display.set_mode([config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT])
		self.font = pygame.font.SysFont("monospace", 36, True)

	def update(self, timeAtRoundStart, map, players, activePlayer):
		self.renderMap(map)
		self.renderWorms(players, activePlayer)
		nextRound = self.calcAndRenderRemainingTime(timeAtRoundStart)
		pygame.display.flip()
		return nextRound

	def calcAndRenderRemainingTime(self, timeAtRoundStart):
		remainingTime = config.TIMEPERROUND - time.clock() + timeAtRoundStart
		if remainingTime >= 10:
			remainingTimeString = str(remainingTime)[0:2]
		else:
			remainingTimeString = '0' + str(remainingTime)[0:1]
		timeLabel = self.font.render(remainingTimeString, 1, (255, 255, 255))
		self._screen.blit(timeLabel, (config.RENDERAREAWIDTH - 50, 0))
		return remainingTime <= 0

	def renderMap(self, map):
		pygame.surfarray.blit_array(self._screen, map)

	def renderWorms(self, players, activePlayer):
		for i in range(len(players)):
			for j in range(len(players[i].worms)):
				colour = (255, 255, 255) if (i == activePlayer and j == players[i].activeWormIdx) else players[i].worms[j]._team_colour
				pygame.draw.rect(self._screen, colour, (players[i].worms[j].corner_col, players[i].worms[j].corner_row, players[i].worms[j].width, players[i].worms[j].height))
