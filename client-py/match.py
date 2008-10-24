class Match:

	date = None
	matchOn = False
	arena = None
	neededWins = 4
	durationSeconds = 120
	players = []
	winner = None	# player

	def __init__(self):
		pass

	def addPlayer(self, player):
		self.players.append(player)

