class Arena:

	players = []

	map = [
			[W,W,W,W,W,W,W,W,W,W,W,W,W],
			[W,B,B,B,B,_,_,_,_,_,_,_,W],
			[W,_,W,_,W,_,W,_,W,_,W,_,W],
			[W,_,_,_,_,_,_,_,_,_,_,_,W],
			[W,_,W,_,W,_,W,_,W,_,W,_,W],
			[W,_,_,B,B,B,B,B,_,_,_,_,W],
			[W,_,W,_,W,B,W,B,W,_,W,_,W],
			[W,_,_,B,_,B,_,B,B,B,_,_,W],
			[W,_,W,_,W,_,W,_,W,_,W,_,W],
			[W,_,_,_,_,B,_,_,_,_,_,_,W],
			[W,_,W,_,W,_,W,_,W,B,W,_,W],
			[W,_,_,_,B,B,B,B,_,_,_,_,W],
			[W,W,W,W,W,W,W,W,W,W,W,W,W]
			];


	def __init__(self):
		randomizeMapContents()
		
	def randomizeMapContents(self):
		# breakable blocks
		# items within blocks
		pass
	
	def checkStatus(self):
		# players have been moved
		# events has been done
		# check what has happened
		# create events
		# create messages
		# send messages to players
