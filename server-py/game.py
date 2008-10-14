class Game:

	GAME_NOT_STARTED_YET = 0
	GAME_STARTED = 1

	players = []
	server = None
	currentArena = None

	def __init__(self, server):
		self.server = server
	
	def addPlayer(self, player):
		self.players.append(player)

	def handleMessage(self, message):
		
		for p in self.players:
			print p
		
		player = self.getPlayerById(message.player_id)
		if not player:
			player = self.getPlayerByAddress(message.address)
	
		print "Message object: " + str(message)
		print "Player object: " + str(player)
		print "Player id: " + player.id
		
		if message.action == message.PLAYER_JOIN:
			self.playerJoins(player, message)
		elif message.action == message.PLAYER_LEAVE:
			self.playerLeaves(player, message)
		elif message.action == message.PLAYER_MOVE:
			self.playerMoves(player, message)
		elif message.action == message.PLAYER_PLANT_BOMB:
			self.playerPlantsBomb(player, message)
		
		# finally send the received message to all players
		# (except original sender)
		self.server.sendMessageToAllPlayers(message)


	def playerStartsGame(self, player, message):
		print "Player <" + player.id + "> starts the game."

	def playerPlantsBomb(self, player, message):
		print "Player <" + player.id + "> plants a bomb at (" + message.parameters[0] + ", " + message.parameters[1] + ")."
		
	def playerMoves(self, player, message):
		print "Player <" + player.id + "> moves to (" + message.parameters[0] + ", " + message.parameters[1] + ")."
		player.position == (message.parameters[0], message.parameters[1])

	def playerPausesGame(self, player, message):
		print "Player <" + player.id + "> pauses the game."

	def playerJoins(self, player, message):
		if player:
			player.id = message.player_id
		print "Player <" + player.id + "> joins the game."
	
	def playerLeaves(self, player, message):
		print "Player <" + player.id + "> leaves the game."
		players.remove(player)
		player = None

	def getPlayerByAddress(self, addr):
		for p in self.players:
			if p.address == addr:
				return p
		return None

	def getPlayerById(self, id):
		for p in self.players:
			if p.id == id:
				return p
		return None

