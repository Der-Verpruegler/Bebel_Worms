#! python

import threading 
import time
import pygame

import config
from GUI import mainRenderer
from UI import userListener
from MAP import mapGenerator
from WORM import worm

running = False
changed = False

def main():
	pygame.init()
	mainLoop()
	
def outputLoop(gui, map, worms):
	global running, changed

	while running:
		time.sleep(0.02)
		gui.update(changed, map.colours, worms)
		changed = False
	return
		
def inputLoop(ui):
	global running, changed
	
	while running:
		time.sleep(0.005)
		running = ui.getNextEvent()
	return
	
def mainLoop():
	global running, changed
	
	gui = mainRenderer.mainRenderer(pygame)
	ui = userListener.userListener(pygame)
	map = mapGenerator.MapBackend()
	worms = []
	
	running = True
	changed = True
	
	outputThread = threading.Thread(target=outputLoop, args=(gui, map, worms,))
	
	outputThread.start()
	inputLoop(ui)
	outputThread.join()
	
	pygame.quit()

main()