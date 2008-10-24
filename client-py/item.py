import pygame

class Item(pygame.Sprite):

	EXTRA_BOMB = 1;
	EXTRA_FLAME = 2;
	KICK = 3;
	TRIPLE_BOMB = 4;
		
	position = (0, 0)
	type = EXTRA_BOMB

	def __init__(self):
		pass

