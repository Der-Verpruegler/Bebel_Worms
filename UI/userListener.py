class userListener:
	def __init__(self, pygame, worms):
		self._pygame = pygame
		self.worms = worms
	
	def getNextEvent(self, worms):
		event = self._pygame.event.poll()
		if event.type == self._pygame.QUIT:
			return False
		pressed = self._pygame.key.get_pressed()
		if pressed[self._pygame.K_LEFT]:
			self.worms[0].move("left")
		elif pressed[self._pygame.K_RIGHT]:
			self.worms[0].move("right")
		elif pressed[self._pygame.K_SPACE]:
			self.worms[0].move("up")
		elif pressed[self._pygame.K_TAB]:
			pass
		return True