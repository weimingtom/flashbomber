import pygame

class Bomb(pygame.sprite.Sprite):
		
	position = (0, 0)
	owner = None	# player
	secondsToGo = 5;
	exploding = False;
		
	def __init__(self, image, position, player):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.position = position
		self.owner = player
		
	def update(self, deltat):
		pass
	
	def burnFuse():
		self.secondsToGo -= 1
		if self.secondsToGo == 0:
			self.explode();

	def explode():
		pass

