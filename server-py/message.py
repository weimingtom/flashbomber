import string

class Message:

	player_id = None
	action = None
	parameters = []
	fieldSeparator = ':'
	address = None

	# actions
	PLAYER_JOIN = 'join'
	PLAYER_LEAVE = 'leave'
	PLAYER_MOVE = 'move'
	PLAYER_PLANT_BOMB = 'plant_bomb'
	PLAYER_STOP_BOMB = 'stop_bomb'
	PLAYER_PAUSE_GAME = 'pause_game'
	PLAYER_START_GAME = 'start_game'
	
	def __init__(self):
		pass

	def __init__(self, message, address):
		self.address = address
		self.parse(message)
	
	def parse(self, message):
		print "Parsing: " + message;
		splitData = message.split(':')
		print splitData
	
		self.player_id = splitData[0]
		self.action = splitData[1]
		self.parameters = splitData[2:]
		
	def __str__(self):
		return "Message <" + self.player_id + self.fieldSeparator + self.action + self.fieldSeparator + string.join(self.parameters, self.fieldSeparator) + "> from address: " + str(self.address)
		
