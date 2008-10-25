from tile import Tile

class Arena:

	name = "The Name Of Arena"
	dimensions = (30, 20)
	players = []
	amountOfExtraBombs = 15
	amountOfExtraFlames = 15
	amountOFKicks = 4

	#
	# this should be just initial character map, but there needs to be also
	# object map.
	#
	initMap = [
			['W','W','W','W','W','W','W','W','W','W','W','W','W'],
			['W','B','B','B','B','_','_','_','_','_','_','_','W'],
			['W','_','W','_','W','_','W','_','W','_','W','_','W'],
			['W','_','_','_','_','_','_','_','_','_','_','_','W'],
			['W','_','W','_','W','_','W','_','W','_','W','_','W'],
			['W','_','_','B','B','B','B','B','_','_','_','_','W'],
			['W','_','W','_','W','B','W','B','W','_','W','_','W'],
			['W','_','_','B','_','B','_','B','B','B','_','_','W'],
			['W','_','W','_','W','_','W','_','W','_','W','_','W'],
			['W','_','_','_','_','B','_','_','_','_','_','_','W'],
			['W','_','W','_','W','_','W','_','W','B','W','_','W'],
			['W','_','_','_','B','B','B','B','_','_','_','_','W'],
			['W','W','W','W','W','W','W','W','W','W','W','W','W']
			];


	map = []

	def __init__(self):
		for row in self.initMap:
			list = []
			for tile in row:
				if tile == 'W':
					list.append(Tile(Tile.SOLID))
				elif tile == 'B':
					list.append(Tile(Tile.BREAKABLE))
				elif tile == '_':	
					list.append(Tile(Tile.EMPTY))
			self.map.append(list)
		
	def randomizeMapContents(self):
		x = y = 0
		for y in range(0, self.dimensions[0]):
			for x in range(0, self.dimensions[1]):
				break
				#tile = map[y][x];
				#if tile.type == Tile.BREAKABLE:
				#	pass
	
	def checkStatus(self):
		# players have been moved
		# events has been done
		# check what has happened
		# create events
		# create messages
		# send messages to players
		pass
	
	def draw():
		pass

