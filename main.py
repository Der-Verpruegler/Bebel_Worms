#! python

import threading 
import time
import pygame
import numpy as np

import config
from GUI import mainRenderer
from UI import userListener
from MAP import mapGenerator
from WORM import worm

running = False
changed = False
worms = np.empty(1, dtype=worm.Worm)
map = []

def main():
	pygame.init()
	mainLoop()
	
def generateWorms():
	global worms, map

	for i in range(config.NUMWORMS):
		worms[i] = worm.Worm(map)
	
def outputLoop(gui):
	global running, changed, worms, map

	while running:
		time.sleep(0.01)
		gui.update(changed, map.colours, worms)
		changed = False
	return
		
def inputLoop(ui, worms):
	global running, changed
	
	while running:
		time.sleep(0.005)
		running = ui.getNextEvent(worms)
	return
	
def mainLoop():
	global running, changed, map, worms
	
	map = mapGenerator.MapBackend()
	generateWorms()
	
	gui = mainRenderer.mainRenderer(pygame)
	ui = userListener.userListener(pygame, worms)

	running = True
	changed = True
	
	outputThread = threading.Thread(target=outputLoop, args=(gui,))
	
	outputThread.start()
	inputLoop(ui, worms)
	outputThread.join()
	
	pygame.quit()

main()