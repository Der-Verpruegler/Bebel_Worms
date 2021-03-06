# pylint: disable=W0312, E1101
import pygame
import config


class userListener:
	def __init__(self):
		pressed = pygame.key.get_pressed()
		self.tabStillPressed = pressed[pygame.K_TAB]
		self.escStillPressed = pressed[pygame.K_ESCAPE]

	def getNextEvent(self, players, activePlayer):
		nextRound = False
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			return (False, False)
		pressed = pygame.key.get_pressed()
		if not pressed[pygame.K_TAB]:
			self.tabStillPressed = False
		if not pressed[pygame.K_ESCAPE]:
			self.escStillPressed = False
		if pressed[pygame.K_SPACE]:
			if pressed[pygame.K_LEFT]:
				pass # Jump left
			elif pressed[pygame.K_RIGHT]:
				pass # Jump right
			else:
				players[activePlayer].getActiveWorm().move("up")
		elif pressed[pygame.K_LEFT]:
			players[activePlayer].getActiveWorm().move("left")
		elif pressed[pygame.K_RIGHT]:
			players[activePlayer].getActiveWorm().move("right")
		elif pressed[pygame.K_TAB] and not self.tabStillPressed:
			players[activePlayer].switch_worm()
			self.tabStillPressed = True
		elif pressed[pygame.K_ESCAPE] and not self.escStillPressed:
			self.escStillPressed = True
			nextRound = True
		return (True, nextRound)
