#!/usr/bin/env python
import pygame
import gc
from ctypes import *

# increase thread priority for this thread

hthread = windll.kernel32.GetCurrentThread()
windll.kernel32.SetThreadPriority(hthread,1)

pygame.init()

screen= pygame.display.set_mode( (800,600), 
pygame.DOUBLEBUF|pygame.HWSURFACE|pygame.FULLSCREEN, 32 )

i= 0
f= pygame.font.Font( r'c:\windows\fonts\arial.ttf', 80 )
s= f.render( 'Scrolling', 1, (0xff,0xee,0x00) )
surf= pygame.Surface( s.get_size(), pygame.SRCALPHA, 32 )
surf.blit( s, (0,0) )
screen.fill( (255,255,255) )
pygame.display.flip()
screen.fill( (255,255,255) )
pygame.display.update()
h=surf.get_height()
gc.disable()
while i< 800:
   screen.fill( (255,255,255), (0,200,800,h) )
   screen.blit( surf, ( i, 200 ) )
   pygame.display.flip()
   pygame.event.poll()
   i+= 5
gc.enable()
pygame.quit()

