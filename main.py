#! python

import threading 
import time
import pygame
import numpy as np
import random

import config
from FRONTEND import mainRenderer
from FRONTEND import userListener
from BACKEND import player
from BACKEND import mapGenerator
from BACKEND import worm

running = False
players = np.empty(config.NUMPLAYERS, dtype=player.Player)
map = []
clock = time.clock()
activePlayer = 0

def main():
	pygame.init()
	mainLoop()
	
def generatePlayers():
	global map, players

	for i in range(config.NUMPLAYERS):
		players[i] = player.Player(map, i)
	
def outputLoop(gui):
	global running, map, players, clock, activePlayer

	while running:
		time.sleep(0.01)
		gui.update(time.clock() - clock, map.colours, players, activePlayer)
		
def inputLoop(ui):
	global running, players
	
	while running:
		time.sleep(0.03) #0.07 is good
		running  = ui.getNextEvent(players, activePlayer)
	
def gravityLoop():
	global running, players
	
	while running:
		time.sleep(0.01)
		for player in players:
			for worm in player.worms:
				worm.move("down")
	
def mainLoop():
	global map, running, activePlayer
	
	map = mapGenerator.MapBackend()
	generatePlayers()
	
	activePlayer = random.randrange(config.NUMPLAYERS)
	
	gui = mainRenderer.mainRenderer()
	ui = userListener.userListener()

	running = True
	
	gravityThread = threading.Thread(target=gravityLoop)
	outputThread = threading.Thread(target=outputLoop, args=(gui,))
	
	gravityThread.start()
	outputThread.start()
	inputLoop(ui)
	outputThread.join()
	
	pygame.quit()

main()