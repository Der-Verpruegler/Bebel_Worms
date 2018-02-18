import config

class mainRenderer:
	def __init__(self, pygame):
		self._pygame = pygame
		self._renderArea = [config.RENDERAREAWIDTH, config.RENDERAREAHEIGHT]
		self._screen = pygame.display.set_mode(self._renderArea)
		
	def update(self):
		self.renderMap()
		self.renderWorms()
		
	def renderMap(self):
		pass
		
	def renderWorms(self):
		pass