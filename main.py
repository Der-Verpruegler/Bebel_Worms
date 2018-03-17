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
		
def inputLoop(ui):
	global running, worms
	
	while running:
		time.sleep(0.07)
		running = ui.getNextEvent(worms)
	
def gravityLoop():
	global running, worms
	
	while running:
		time.sleep(0.01)
		for worm in worms:
			worm.move("down")
	
def mainLoop():
	global running, map, worms
	
	map = mapGenerator.MapBackend()
	generateWorms()
	
	gui = mainRenderer.mainRenderer(pygame)
	ui = userListener.userListener(pygame, worms)

	running = True
	
	gravityThread = threading.Thread(target=gravityLoop)
	outputThread = threading.Thread(target=outputLoop, args=(gui,))
	
	gravityThread.start()
	outputThread.start()
	inputLoop(ui)
	outputThread.join()
	
	pygame.quit()

main()