import pygame, random

# ----------------------------------------------------------------------
# Bonus Item 
# ----------------------------------------------------------------------
class BonusItem(pygame.sprite.Sprite):

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

# ----------------------------------------------------------------------
# Magic Mushroom 
# ----------------------------------------------------------------------
class MagicMushroom(pygame.sprite.Sprite):

	NO_EFFECT = 0
	SLOW_MOVEMENT = 1		# first effect
	FAST_MOVEMENT = 2
	SLOW_BOMBS = 3
	FAST_BOMBS = 4
	TELEPORT = 5
	REVERSE_MOVEMENT = 6
	FORCED_BOMB_PLANTING = 7
	NO_BOMB_PLANTING = 8		# last effect

	position = (0, 0)
	type = 0

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.position = position
		self.type = random.randint(1, 8)		# first and last effect
			
	def update(self, deltat):
		pass

# ----------------------------------------------------------------------
# Exploding Bomb 
# ----------------------------------------------------------------------
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

