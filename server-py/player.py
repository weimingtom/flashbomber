import socket

class Player:

	id = ""

	connection = None
	address = None
	
	position = (0, 0)
	extraBombs = 0
	extraFlames = 0
	
	def __init__(self, conn, addr):
		self.connection = conn
		self.address = addr
		
	def sendMessage(self, message):
		try:
			self.connection.send(message)
		except socket.error, msg:
			self.connection = None
			print "ERROR WHILE SENDING TO:", self.address
			raise E('Player connection failed!')			
	
	def __del__(self):
		if self.connection:
			self.connection.close()

	def __str__(self):
		if self.id:
			return "Player <" + self.id + "> from address " + str(self.address)
		else:
			return "Player <unknown> from address " + str(self.address)
			
