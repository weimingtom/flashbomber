import pygame

class Item(pygame.sprite.Sprite):

	EXTRA_BOMB = 1;
	EXTRA_FLAME = 2;
	KICK = 3;
	TRIPLE_BOMB = 4;
		
	position = (0, 0)
	type = EXTRA_BOMB

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.position = position

	def update(self, deltat):
		pass

