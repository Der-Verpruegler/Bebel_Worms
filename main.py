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
worms = np.empty(config.NUMWORMS, dtype=worm.Worm)
map = []

def main():
	pygame.init()
	mainLoop()
	
def generateWorms():
	global map, worms

	for i in range(config.NUMWORMS):
		worms[i] = worm.Worm(map)
	
def outputLoop(gui):
	global running, map, worms

	while running:
		time.sleep(0.01)
		gui.update(map.colours, worms)
	return
		
def inputLoop(ui, worms):
	global running
	
	while running:
		time.sleep(0.005)
		running = ui.getNextEvent(worms)
		print(worms[0].corner_col, worms[0].corner_row)
	return
	
def mainLoop():
	global running, map, worms
	
	map = mapGenerator.MapBackend()
	generateWorms()
	
	gui = mainRenderer.mainRenderer(pygame)
	ui = userListener.userListener(pygame, worms)

	running = True
	
	outputThread = threading.Thread(target=outputLoop, args=(gui,))
	
	outputThread.start()
	inputLoop(ui, worms)
	outputThread.join()
	
	pygame.quit()

main()