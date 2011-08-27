"""
mechpy keyboard controller (sends keyboard events)
"""

import events
import pygame
import eventmanager
from pygame.locals import *

class KeyboardController:
    
    def __init__(self):
        self.name = "CPU Controller"
        self.evManager = eventmanager.evManager
    
    def Notify(self, event):
        if isinstance( event, events.TickEvent ):
            for event in pygame.event.get():
                if event.type == QUIT or \
                   event.type == KEYDOWN and event.key == K_ESCAPE:
                    quitEvent = events.QuitEvent()
                    self.evManager.Post( quitEvent )
                #handle other keyboard events
            
