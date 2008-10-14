import socket, sys, time
from player import Player
from message import Message
from game import Game

class Server:
	
	SERVERNAME = 'Java-teamserver'
	HOST = 'localhost'
	PORT = 50007
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#players = []
	game = None
	
	def __init__(self):
		self.socket.bind((self.HOST, self.PORT))
		self.socket.listen(1)
		self.socket.setblocking(0)
		self.game = Game(self)
	
	def start(self):
		print "Listening to connections at " + self.HOST + ":" + str(self.PORT)
		self.mainLoop()

	def stop(self):
		print "Server shutdown ..."
		self.socket.close()
		sys.exit(0);
		
	#def addPlayer(self, player):
	#	self.players.append(player)
		
	def sendMessageToAllPlayers(self, message):
		for p in self.game.players:
			try:
				p.sendMessage(message)
			except Exception, e:
				self.game.players.remove(p)
	
	def mainLoop(self):
		while 1:
			time.sleep(1)	# wait a sec
			print "." 
			
			updateMessage = "1 sec"
			#updateMessage = updateGameArena()	
			
			# wait for players to join/connect
			conn = None
			try:
				conn, addr = self.socket.accept()
				#conn.setblocking(0)
				if conn:		
					p = Player(conn, addr)
					self.game.addPlayer(p)		# add unidentified player
			except Exception, e:
				pass
			
			# wait for player messages
			if conn:
				data = conn.recv(1024)
				if not data:
					print "no data"
				else:
					# parse msg
					m = Message(data, addr)
					self.game.handleMessage(m)
			
			self.sendMessageToAllPlayers(updateMessage)
	
	def __del__(self):
		self.stop()

