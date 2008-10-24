import pygame

class Bomb(pygame.Sprite):
		
	position = (0, 0)
	owner = None	# player
	secondsToGo = 5;
	exploding = False;
		
	def __init__(self, position, player):
		self.position = position
		self.owner = player

	def burnFuse():
		self.secondsToGo -= 1
		if self.secondsToGo == 0:
			self.explode();

	def explode():
		pass

