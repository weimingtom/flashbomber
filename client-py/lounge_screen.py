#!/usr/bin/env python
import pygame
import os, sys
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = None
screenW = 800
screenH = 600
tileSize = 32
k_up = k_down = k_left = k_right = 0

map = [
		['W','W','W','W','W','W','W','W','W','W','W','W','W'],
		['W','B','B','B','B','_','_','_','_','_','_','_','W'],
		['W','_','W','_','W','_','W','_','W','_','W','_','W'],
		['W','_','_','_','_','_','_','_','_','_','_','_','W'],
		['W','_','W','_','W','_','W','_','W','_','W','_','W'],
		['W','_','_','B','B','B','B','B','_','_','_','_','W'],
		['W','_','W','_','W','B','W','B','W','_','W','_','W'],
		['W','_','_','B','_','B','_','B','B','B','_','_','W'],
		['W','_','W','_','W','_','W','_','W','_','W','_','W'],
		['W','_','_','_','_','B','_','_','_','_','_','_','W'],
		['W','_','W','_','W','_','W','_','W','B','W','_','W'],
		['W','_','_','_','B','B','B','B','_','_','_','_','W'],
		['W','W','W','W','W','W','W','W','W','W','W','W','W']
		];

def drawArena():
	tile_solid = pygame.image.load('images/tile_desert_solid.png')
	tile_empty = pygame.image.load('images/tile_desert_empty.png')
	tile_breakable = pygame.image.load('images/tile_desert_breakable.png')
	
	x = 0
	y = 0
	for row in map:
		for tile in row:
			if tile == 'W':
				screen.blit(tile_solid, (x, y))
			elif tile == 'B':
				screen.blit(tile_breakable, (x, y))
			elif tile == '_':	
				screen.blit(tile_empty, (x, y))
			x += tileSize
		x = 0
		y += tileSize

	pygame.display.flip()

playerX = 100
playerY = 100
playerMovingUp = False
playerMovingDown = False
playerMovingLeft = False
playerMovingRight = False

def clearMovement():
	global playerMovingUp, playerMovingDown, playerMovingLeft, playerMovingRight
	playerMovingUp = False
	playerMovingDown = False
	playerMovingLeft = False
	playerMovingRight = False

def drawPlayer():
	global screen, playerX, playerY
	player = pygame.image.load('images/player_temp.png')
	screen.blit(player, (playerX, playerY))
	
def main():
	global playerX, playerY, playerMovingUp, playerMovingDown, playerMovingLeft, playerMovingRight
	
	if playerMovingUp:
		playerY -= 2
	elif playerMovingDown:
		playerY += 2
	elif playerMovingLeft:
		playerX -= 2
	elif playerMovingRight:
		playerX += 2
	
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		down = event.type == KEYDOWN # key down or up?
		print down
		if down:
			if event.key == K_RIGHT:
				playerMovingRight = True
			elif event.key == K_LEFT:
				playerMovingLeft = True
			elif event.key == K_UP:
				playerMovingUp = True
			elif event.key == K_DOWN:
				playerMovingDown = True
			elif event.key == K_ESCAPE: sys.exit(0) # quit the game
		else:
			clearMovement()		

	drawPlayer()
	

def main():
	global screen
	pygame.init()
	pygame.mouse.set_visible(0)
	#pygame.display.set_icon(pygame.image.load(data.filepath("icon.gif")))
	pygame.display.set_caption("PyBomber 2008")
	clock = pygame.time.Clock()
	FRAMES_PER_SECOND = 100
	
	try:
		screen = pygame.display.set_mode((screenW, screenH))
		
		# This should show a blank 200 by 200 window centered on the screen
		
		drawArena()
		while 1:		
			deltat = clock.tick(FRAMES_PER_SECOND)
	
			main()
	
			pygame.display.flip()
			#evt = pygame.event.wait()
			#if evt.type == pygame.QUIT:
			#	break
	finally:
		pygame.quit()  # Keep this IDLE friendly

