"""
mechpy cursor controller (sends cursor events)
"""

import events
import pygame
import eventmanager
from pygame.locals import *

class CursorController:
    
    def __init__(self):
        self.name = "Cursor Controller"
        self.evManager = eventmanager.evManager
    
    def Notify(self, event):
        if isinstance( event, events.TickEvent ):
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    cursorEvent = events.CursorEvent()
                    self.evManager.Post( cursorEvent )
