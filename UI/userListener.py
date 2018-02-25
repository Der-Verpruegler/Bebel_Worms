class userListener:
	def __init__(self, pygame):
		self._pygame = pygame
	
	def getEvents(self):
		for event in self._pygame.event.get():
			if event.type == self._pygame.QUIT:
				return False
			elif event.key == self._pygame.K_LEFT:
				pass
			elif event.key == self._pygame.K_RIGHT:
				pass
			elif event.key == self._pygame.K_TAB:
				pass
		return True