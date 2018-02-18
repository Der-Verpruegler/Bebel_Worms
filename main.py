#! python
import pygame

import config
from GUI import mainRenderer
from UI import userListener

def main():
	pygame.init()
	
	clock = pygame.time.Clock()
	gui = mainRenderer.mainRenderer(pygame)
	ui = userListener.userListener(pygame)
	
	mainLoop(clock, gui, ui)
	
def mainLoop(clock, gui, ui):
	running = True
	while(running):
		clock.tick(config.ITERATIONSPERSECOND)
		running = ui.getEvents()
		gui.update()
	
main()