class userListener:
	def __init__(self, pygame):
		self._pygame = pygame
	
	def getNextEvent(self):
		event = self._pygame.event.poll()
		if event.type == self._pygame.QUIT:
			return False
		if event.type == self._pygame.K_LEFT:
			pass
		elif event.type == self._pygame.K_RIGHT:
			pass
		elif event.type == self._pygame.K_TAB:
			pass
		return True