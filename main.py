#! python

import threading 
import time
import pygame

import config
from GUI import mainRenderer
from UI import userListener
from MAP import mapGenerator

running = True

def main():
	pygame.init()
	mainLoop()
	
def outputLoop(gui, map, worms):
	global running
	changed = True

	while running:
		time.sleep(0.02)
		gui.update(changed, map.colours, worms)
		changed = False
	return
		
def inputLoop(ui):
	global running
	while running:
		time.sleep(0.005)
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.K_LEFT:
			print(event)
		elif event.type == pygame.K_RIGHT:
			print(event)
		elif event.type == pygame.K_TAB:
			print(event)
	return
	
def mainLoop():
	gui = mainRenderer.mainRenderer(pygame)
	ui = userListener.userListener(pygame)
	map = mapGenerator.MapBackend()
	worms = []
	outputThread = threading.Thread(target=outputLoop, args=(gui, map, worms,))
	
	outputThread.start()
	inputLoop(ui)
	outputThread.join()
	
	pygame.quit()

main()