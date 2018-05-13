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
			
		movementList = []
		if pressed[pygame.K_SPACE]:
			if pressed[pygame.K_LEFT]:
				for i in range(0, config.WORM_JUMP_HEIGHT / 2):
					movementList.append("up")
					movementList.append("left")
			elif pressed[pygame.K_RIGHT]:
				for i in range(0, config.WORM_JUMP_HEIGHT / 2):
					movementList.append("up")
					movementList.append("right")
			else:
				for i in range(0, config.WORM_JUMP_HEIGHT):
					movementList.append("up")
		elif pressed[pygame.K_LEFT]:
			movementList.append("left")
		elif pressed[pygame.K_RIGHT]:
			movementList.append("right")
		elif pressed[pygame.K_TAB] and not self.tabStillPressed:
			players[activePlayer].switch_worm()
			self.tabStillPressed = True
		elif pressed[pygame.K_ESCAPE] and not self.escStillPressed:
			self.escStillPressed = True
			nextRound = True
			
		players[activePlayer].getActiveWorm().move(movementList)
				
		for player in players:
			for worm in player.worms:
				worm.move(["down"])
				
		return (True, nextRound)
