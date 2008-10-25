#!/usr/bin/env python
import pygame
import os, sys
import gc
import lounge_screen

from ctypes import *

from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = None
screenW = 800
screenH = 600
tileSize = 32
screen = None

sinewave = [
	100,97,95,92,90,87,85,82,80,78,75,73,70,68,66,63,
	61,59,57,54,52,50,48,46,44,42,40,38,36,34,32,30,
	29,27,25,24,22,20,19,18,16,15,14,12,11,10,9,8,
	7,6,5,4,4,3,2,2,1,1,1,0,0,0,0,0,
	0,0,0,0,0,0,1,1,2,2,3,3,4,5,6,6,
	7,8,9,11,12,13,14,15,17,18,20,21,23,24,26,28,
	29,31,33,35,37,39,41,43,45,47,49,51,53,55,58,60,
	62,65,67,69,72,74,76,79,81,84,86,88,91,93,96,98,
	101,103,106,108,111,113,115,118,120,123,125,127,130,132,134,137,
	139,141,144,146,148,150,152,154,156,158,160,162,164,166,168,170,
	171,173,175,176,178,179,181,182,184,185,186,187,188,190,191,192,
	193,193,194,195,196,196,197,197,198,198,199,199,199,199,199,199,
	199,199,199,199,199,198,198,198,197,197,196,195,195,194,193,192,
	191,190,189,188,187,185,184,183,181,180,179,177,175,174,172,170,
	169,167,165,163,161,159,157,155,153,151,149,147,145,142,140,138,
	136,133,131,129,126,124,121,119,117,114,112,109,107,104,102,100
]

scrollText = "             *GBOMBER 2008*          CODING BY THE G-MEN          PRESS ANYKEY TO CONTINUE          POWERED BY PYTHON        AND THE AMAZING         ... PYGAME LIB     "

sineScrollerIndex = 0
sineScrollerX = 0
textIndex = 0
def waveScroller():
	global sineScrollerX, sineScrollerIndex, screen, sineScrollerSurface, screenH, screenW, textIndex, scrollTextSurface
	
	step = 4	#px
	sineIndex = sineScrollerIndex
	for index in range (0, screenW/step):
		subsurface = sineScrollerSurface.subsurface((index * step, 0, step, 120))
		screen.blit(subsurface, (0 + (index * step), 200 + (int(sinewave[sineIndex] * 1.2) ) ))
		sineIndex += 1
		if sineIndex >= 255:
			sineIndex = 0

	sineScrollerIndex += 3
	if sineScrollerIndex >= 255:
		sineScrollerIndex = 0

	#
	# make better system here with modulo offsets (width/step)
	#
	sineScrollerX -= 5
	if sineScrollerX < -55:		# width of one character (guessed)
		textIndex += 1			
		if textIndex > (len(scrollText) - 1):
			textIndex = 0
		sineScrollerX = 0
		scrollTextSurface.fill((0,0,0))
		scrollTextSurface = font.render(scrollText[textIndex:], 0, (200,200,200))
	sineScrollerSurface.fill((0,0,0))
	sineScrollerSurface.blit(scrollTextSurface, (sineScrollerX, 0))

beam = []
def setupBeam():
	global beam	
	for i in range(0, 16):
		beam.append((0, i*16, 0))
	for i in range(15, 0, -1):
		beam.append((0, i*16, 0))

beamCenter = 270

def drawBeam(sinepos):
	global screen
	y = beamCenter + sinewave[sinepos]
	for color in beam:
		pygame.draw.line(screen, color, (0, y), (screenW-1, y), 1)
		y += 1


# increase thread priority for this thread

hthread = windll.kernel32.GetCurrentThread()
windll.kernel32.SetThreadPriority(hthread,1)

pygame.init()
pygame.mouse.set_visible(0)
#pygame.display.set_icon(pygame.image.load(data.filepath("icon.gif")))
pygame.display.set_caption("PyBomber 2008")
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 150

direction = False

#start positions in sine index < 255
beams = [0, 15, 30, 45, 60, 75, 90]
beamColors = [(255, 0, 255), (255, 255, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)]

def updateBeams():
	i = 0
	for beam in beams:
		if beam >= 254:
			beams[i] = 0
		else:
			beams[i] = beam + 2
		i += 1
		
	index = 0
	for beam in beams:
		drawBeam(beam)
		index += 1

font = pygame.font.Font('c:/Windows/Fonts/DejaVuMonoSansBold.ttf', 100)
scrollTextSpecific = None
scrollColors = [140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 250, 245, 240, 235, 230, 225, 220, 215, 210, 205, 200, 195, 190, 185, 180, 175, 170, 165, 160, 155, 150, 145, 140]
currentScrollColor = 0
scrollX = screenW

sineScrollerSurface = pygame.Surface((screenW, 120))
sineScrollerSurface.set_colorkey((0,0,0))
scrollTextSurface = font.render(scrollText, 0, (200,200,200))

def scroller():
	global screen, scrollX, scrollTextSpecific, currentScrollColor
	color = scrollColors[currentScrollColor]
	scrollTextSpecific = font.render("=== PYTHON/BOMBER 2008 GAME ===", 0, (color,color,color))
	currentScrollColor += 1
	if currentScrollColor >= len(scrollColors):
		currentScrollColor = 0
		
	screen.blit(scrollTextSpecific, (scrollX,400))
	scrollX -= 5
	if scrollX <= 0:
		scrollX = screenW

logoIndex = 0
def drawLogo():
	global screen, logoIndex	
	#logo = pygame.image.load('images/gbomber_logo.png')
	logo = pygame.image.load('images/gbomber_logo_green.png')
	xPos = (screenW - logo.get_width() - 600)/2
	xPos += int(sinewave[logoIndex] * 3)
	logoIndex += 4
	if logoIndex >= 255:
		logoIndex = 0
		
	screen.blit(logo, (xPos, 50))

def makeWater():
	global screen
	subsurface = screen.subsurface((0, 400, 800, 100))
	water = pygame.transform.flip(subsurface, False, True)
	pxarray = pygame.PixelArray(water)
		
	water = pxarray.make_surface()	
	del(pxarray)
	water.set_alpha(100)
	water.set_colorkey((0,0,0))
	screen.blit(water, (0, 500))
	
def main():
	global screen
	try:
		screen = pygame.display.set_mode((screenW, screenH), pygame.DOUBLEBUF | pygame.HWSURFACE, 16)	#| pygame.FULLSCREEN 
		
		setupBeam()
		gc.disable()
	
		looping = True
		while 1:		
			pygame.display.flip()
			deltat = clock.tick(FRAMES_PER_SECOND)
			#print deltat
	
			# clear screen
			screen.fill((0,0,0))
	
			drawLogo()
			updateBeams()
			waveScroller()
			screen.fill((0,0,50), (0, 500, 800, 100))
			makeWater()
			
			# draw screen
	
			for event in pygame.event.get():
				if not hasattr(event, 'key'): continue
				down = event.type == KEYDOWN # key down or up?
				if down:
					if event.key == K_ESCAPE:
						sys.exit(0) # quit the game
					else:
						looping = False
						break
						
		# after breaking from the while loop, go to lounge screen
		lounge_screen.main()
	
	finally:
		gc.enable()
	
		pygame.quit()  # Keep this IDLE friendly

