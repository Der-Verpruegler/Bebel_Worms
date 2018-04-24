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
clock = 0
activePlayer = 0

def main():
	pygame.init()
	mainLoop()
	
def generatePlayers():
	global map, players

	for i in range(config.NUMPLAYERS):
		players[i] = player.Player(map, i)
	
def initiateNextRound():
	global activePlayer, clock
	clock = time.clock()
	activePlayer = (activePlayer + 1) % config.NUMPLAYERS
	
def outputLoop(gui):
	global running, map, players, clock, activePlayer

	while running:
		time.sleep(0.01)
		nextRound = gui.update(clock, map.colours, players, activePlayer)
		if nextRound:
			initiateNextRound()
		
def inputLoop(ui):
	global running, players, activePlayer
	
	while running:
		time.sleep(0.03) #0.07 is good
		running, nextRound  = ui.getNextEvent(players, activePlayer)
		if nextRound:
			initiateNextRound()
	
def mainLoop():
	global map, running, activePlayer
	
	map = mapGenerator.MapBackend()
	generatePlayers()
	
	activePlayer = random.randrange(config.NUMPLAYERS)
	
	gui = mainRenderer.mainRenderer()
	ui = userListener.userListener()

	running = True
	
	outputThread = threading.Thread(target=outputLoop, args=(gui,))
	
	outputThread.start()
	initiateNextRound()
	inputLoop(ui)
	outputThread.join()
	
	pygame.quit()

main()