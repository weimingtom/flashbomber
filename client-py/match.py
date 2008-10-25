class Match:

	date = None
	matchOn = False
	arena = None
	neededVictories = 4
	durationSeconds = 120
	players = []
	winner = None	# player
	over = False

	def __init__(self):
		pass

	def addPlayer(self, player):
		self.players.append(player)

	def isOver(self):
		for p in self.players:
			if p.victories >= self.neededVictories:
				self.over = True
			
		return self.over;
