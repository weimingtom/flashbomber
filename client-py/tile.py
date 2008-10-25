import pygame

class Tile(pygame.sprite.Sprite):

	SOLID = 1
	BREAKABLE = 2
	EMPTY = 3
	
	type = 1		# default type = SOLID
	item = None
	image = None
	size = 0

	def __init__(self, type):
		self.type = type
		if type == self.SOLID:
			self.image = pygame.image.load('images/tile_desert_solid.png')
		elif type == self.BREAKABLE:
			self.image = pygame.image.load('images/tile_desert_breakable.png')
		elif type == self.EMPTY:
			self.image = pygame.image.load('images/tile_desert_empty.png')
		self.size = self.image.get_width()

	def update(self, collisions):
		pass
	
