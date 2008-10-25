import pygame

class Player(pygame.sprite.Sprite):

	RED = 1
	BLUE = 2
	WHITE = 3
	BLACK = 4
	GREEN = 5

	NORMAL_STATE = 1
	MAGIC_STATE = 2
	state = NORMAL_STATE

	playerName = "unnamedPlayer"
	color = 0
	startPosition = (0, 0)
	currentPosition = (0, 0)
	amountOfBombs = 1
	lenghtOfFlames = 2
	hasKick = False
	hasMulti = False
	victories = 0

	movingLeft = False
	movingRight = False
	movingUp = False
	movingDown = False

	def moveLeft(self):
		self.movingLeft = True
		
	def moveRight(self):
		self.movingRight = True
		
	def moveUp(self):
		self.movingUp = True
		
	def moveDown(self):
		self.movingDown = True

	def clearMovement(self):
		self.movingLeft = False
		self.movingRight = False
		self.movingUp = False
		self.movingDown = False
	
	def dropBomb(self):
		pass
		
	def stopBomb(self):
		pass
		
	def __init__(self, color, image, position):		
		pygame.sprite.Sprite.__init__(self)
		self.color = color
		self.image = pygame.image.load(image)	# src_image?
		self.position = position
		self.rect = pygame.Rect(self.image.get_rect())
		self.rect.center = position

	def update(self, deltat):
		x, y = self.position
		if self.movingLeft:
			x += -4
		elif self.movingRight:			
			x += 4
		elif self.movingUp:			
			y += -4
		elif self.movingDown:			
			y += 4
		
		self.position = (x, y)
		self.rect = self.image.get_rect()
		self.rect.center = self.position

