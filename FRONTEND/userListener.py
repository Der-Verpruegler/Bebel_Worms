import config

import pygame

class userListener:
	def __init__(self):
		pressed = pygame.key.get_pressed()
		self.tabStillPressed = pressed[pygame.K_TAB]
	
	def getNextEvent(self, players, activePlayer):
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			return False
		pressed = pygame.key.get_pressed()
		if not pressed[pygame.K_TAB]:
			self.tabStillPressed = False
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
		return True
