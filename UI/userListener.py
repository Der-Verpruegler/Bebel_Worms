class userListener:
	def __init__(self, pygame):
		self._pygame = pygame
	
	def getEvents(self):
		for event in self._pygame.event.get():
			if event.type == self._pygame.QUIT:
				return False
		return True