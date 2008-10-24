import pygame

class Player(pygame.Sprite):

	RED = 1;
	BLUE = 2;
	WHITE = 3;
	BLACK = 4;
	GREEN = 5;

	NORMAL_STATE = 1;
	SKULL_STATE = 2;
	state = NORMAL_STATE

	playerName = ""
	color = (0, 0, 0)
	startPosition = (0, 0)
	currentPosition = (0, 0)
	amountOfBombs = 1;
	lenghtOfFlames = 2;
	hasKick = False;
	hasMulti = False;

	def moveLeft():
		pass
		
	def moveRight():
		pass
		
	def moveUp():
		pass
		
	def moveDown():
		pass
		
	def dropBomb():
		pass
		
	def stopBomb():
		pass
		
	def draw():
		pass

