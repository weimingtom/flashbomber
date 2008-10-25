#!/usr/bin/env python
import pygame
import os, sys
from pygame.locals import *
from player import Player
import inter_results_screen
import final_results_screen
from arena import Arena
from match import Match

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = None
screenW = 800
screenH = 600
tileSize = 32

arenaSurface = pygame.Surface((screenW, screenH))
def drawArena():
	global arena, arenaSurface
		
	x = y = 0
	for row in arena.map:
		for tile in row:
			arenaSurface.blit(tile.image, (x, y))
			x += tileSize
		x = 0
		y += tileSize

def checkKeyboard():
	global player

	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		#print event.type
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

	match = Match()
	arena = Arena()
	screen.fill((0,0,0))
	drawArena()
	
	looping = True
	while looping:		
		deltat = clock.tick(FRAMES_PER_SECOND)
		
		player_group.clear(screen, arenaSurface)
		checkKeyboard()
		screen.blit(arenaSurface, (0, 0))

		player_group.update(deltat)
		player_group.draw(screen)

		pygame.display.flip()
		
		#if match.roundIsOver():
		#	inter_results_screen.main()
		#	break
		
		if match.isOver():
			break
			
		#evt = pygame.event.wait()
		#if evt.type == pygame.QUIT:
		#	break
		
	final_results_screen.main()	
	
finally:
	pygame.quit()  # Keep this IDLE friendly

