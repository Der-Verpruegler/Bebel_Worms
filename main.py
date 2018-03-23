#! python

import threading 
import time
import pygame
import numpy as np
import random

import config
from FRONTEND import mainRenderer
from FRONTEND import userListener
from BACKEND import mapGenerator
from BACKEND import worm

running = False
worms = np.empty(config.NUMWORMS, dtype=worm.Worm)
map = []
activeWorm = random.randrange(config.NUMWORMS)
clock = time.clock()

def main():
	pygame.init()
	mainLoop()
	
def generateWorms():
	global map, worms

	for i in range(config.NUMWORMS):
		worms[i] = worm.Worm(map)
	
def outputLoop(gui):
	global running, map, worms, clock

	while running:
		time.sleep(0.01)
		gui.update(time.clock() - clock, map.colours, worms, activeWorm)
		
def inputLoop(ui):
	global running, worms, activeWorm
	
	while running:
		time.sleep(0.03) #0.07 is good
		running, activeWorm = ui.getNextEvent(worms, activeWorm)
	
def gravityLoop():
	global running, worms
	
	while running:
		time.sleep(0.01)
		for worm_set in worms:
			worm_set.move("down")
	
def mainLoop():
	global running, map, worms
	
	map = mapGenerator.MapBackend()
	generateWorms()
	
	gui = mainRenderer.mainRenderer()
	ui = userListener.userListener(worms)

	running = True
	
	gravityThread = threading.Thread(target=gravityLoop)
	outputThread = threading.Thread(target=outputLoop, args=(gui,))
	
	gravityThread.start()
	outputThread.start()
	inputLoop(ui)
	outputThread.join()
	
	pygame.quit()

main()