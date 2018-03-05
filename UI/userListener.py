class userListener:
	def __init__(self, pygame):
		self._pygame = pygame
	
	def getEvents(self):
		while(1):
			for event in self._pygame.event.get():
				print(event)
				if event.type == self._pygame.QUIT:
					return False
				elif event.type == self._pygame.K_LEFT:
					pass
				elif event.type == self._pygame.K_RIGHT:
					pass
				elif event.type == self._pygame.K_TAB:
					pass