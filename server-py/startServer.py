#!/usr/bin/env python
import sys
from server import Server

print """
===== FlashBomber 2008 Server =====

Software written by Mikko Saarela, 2008.

(Press Ctrl-Break to stop the server.)

Copyright, GNU General Public Licence version 3.

Server started ...
"""

server = Server();
server.start();

