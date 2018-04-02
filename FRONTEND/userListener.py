import pygame

class userListener:
	def __init__(self):
		pass
	
	def getNextEvent(self, players):
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			return False
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT]:
			players[0].worms[0].move("left")
		elif pressed[pygame.K_RIGHT]:
			players[0].worms[0].move("right")
		elif pressed[pygame.K_SPACE]:
			players[0].worms[0].move("up")
		elif pressed[pygame.K_TAB]:
			pass
		return True