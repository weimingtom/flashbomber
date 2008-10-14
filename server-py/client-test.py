#!/usr/bin/env python
import socket

HOST = 'localhost'    		# The remote host
PORT = 50007             	# The remote port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Test player join
s.send("player_1:join");

# Test player location change
#s.send("player_1:move:pos_x:pos_y");

# Test player location change
#s.send("player_1:bomb:pos_x:pos_y");


#
# Main loop
#
while 1:
	
	data = s.recv(1024)
	if not data:
		continue
	else:
		print 'Received from server:', repr(data)

s.close()


