#!/usr/bin/env python
import pygame
import os, sys
from pygame.locals import *
from player import Player

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = None
screenW = 800
screenH = 600
tileSize = 32
k_up = k_down = k_left = k_right = 0

#
# this should be just initial character map, but there needs to be also object
# map.
#
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

#
# fix this so that it used the object-map instead of character-map
#
def drawArena():
	tile_solid = pygame.image.load('images/tile_desert_solid.png')
	tile_empty = pygame.image.load('images/tile_desert_empty.png')
	tile_breakable = pygame.image.load('images/tile_desert_breakable.png')
	
	x = y = 0
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

#
# put this into main loop, or at least rename this method
#
def main():
	global player
	
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		print event.type
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				player.moveRight()
			elif event.key == K_LEFT:
				player.moveLeft()
			elif event.key == K_UP:
				player.moveUp()
			elif event.key == K_DOWN:
				player.moveDown()
			elif event.key == K_ESCAPE: sys.exit(0) # quit the game
		elif event.type == KEYUP:
			player.clearMovement()

def newMain():
	global player

	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		print event.type
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE: sys.exit(0) # quit the game
		elif event.type == KEYUP:
			player.clearMovement()

	if (pygame.key.get_pressed()[K_RIGHT]) and (not pygame.key.get_pressed()[K_LEFT]):
			player.moveRight()
	elif (pygame.key.get_pressed()[K_LEFT]) and (not pygame.key.get_pressed()[K_RIGHT]):
			player.moveLeft()
	elif (pygame.key.get_pressed()[K_UP]) and (not pygame.key.get_pressed()[K_DOWN]):
			player.moveUp()
	elif (pygame.key.get_pressed()[K_DOWN]) and (not pygame.key.get_pressed()[K_UP]):
			player.moveDown()
		

#
# move this stuff into main method
#
pygame.init()
pygame.mouse.set_visible(0)
#pygame.display.set_icon(pygame.image.load(data.filepath("icon.gif")))
pygame.display.set_caption("PyBomber 2008")
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 40

try:
	screen = pygame.display.set_mode((screenW, screenH))
	
	rect = screen.get_rect()
	player = Player(Player.RED, 'images/player_temp.png', rect.center)
	player_group = pygame.sprite.RenderPlain(player)

	looping = True
	while looping:		
		deltat = clock.tick(FRAMES_PER_SECOND)
		newMain()
		
		screen.fill((0,0,0))
		drawArena()

		player_group.update(deltat)
		player_group.draw(screen)

		pygame.display.flip()
		#evt = pygame.event.wait()
		#if evt.type == pygame.QUIT:
		#	break
finally:
	pygame.quit()  # Keep this IDLE friendly





