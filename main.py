#! python
import pygame

import config
from GUI import mainRenderer
from UI import userListener
from MAP import mapGenerator
from WORM import worm

def main():
	pygame.init()
	
	clock = pygame.time.Clock()

	gui = mainRenderer.mainRenderer(pygame)
	ui = userListener.userListener(pygame)
	
	mainLoop(clock, gui, ui)
	
def mainLoop(clock, gui, ui):
	map = mapGenerator.MapBackend()
	worms = []
	running = True
	changed = True
	while(running):
		clock.tick(config.ITERATIONSPERSECOND)
		running = ui.getEvents()
		gui.update(changed, map.colours, worms)
		changed = False
	pygame.quit()

main()