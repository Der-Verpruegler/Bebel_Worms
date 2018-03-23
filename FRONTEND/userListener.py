import config

import pygame

class userListener:
	def __init__(self, worms):
		self.worms = worms
		pressed = pygame.key.get_pressed()
		self.tabStillPressed = pressed[pygame.K_TAB]
	
	def getNextEvent(self, worms, activeWorm):
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			return (False, -1)
		pressed = pygame.key.get_pressed()
		if not pressed[pygame.K_TAB]:
			self.tabStillPressed = False
		if pressed[pygame.K_SPACE]:
			if pressed[pygame.K_LEFT]:
				pass # Jump left
			if pressed[pygame.K_RIGHT]:
				pass # Jump right
			self.worms[activeWorm].move("up")
		elif pressed[pygame.K_LEFT]:
			self.worms[activeWorm].move("left")
		elif pressed[pygame.K_RIGHT]:
			self.worms[activeWorm].move("right")
		elif pressed[pygame.K_TAB] and not self.tabStillPressed:
			activeWorm = (activeWorm + 1) % config.NUMWORMS
			self.tabStillPressed = True
		return (True, activeWorm)