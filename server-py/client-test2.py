#!/usr/bin/env python
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Test player join
#s.send("player_2:join:pos_x:pos_y");

# Test player location change
s.send("player_2:move:pos_x:pos_y");

# Test player location change
#s.send("player_2:bomb:pos_x:pos_y");


#
# Main loop
#
while 1:
	
	data = s.recv(1024)
	print 'Received from server:', repr(data)

s.close()


