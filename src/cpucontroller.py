"""
mechpy CPU controller (sends cpu tick events)
"""

#
# Load logging
#
import logging, sys, os, util

log = logging.getLogger(__name__)

log.info("Loading CPU Controller...")

import pygame
import events
import eventmanager

class CPUController:
    
    def __init__(self):
        self.name = "CPU Controller"
        self.evManager = eventmanager.evManager
    
    def Run(self):
        clock = pygame.time.Clock()
        self.keepGoing = True
        while self.keepGoing:
            event = events.TickEvent()
            clock.tick(30) #safety tick bound
            self.evManager.Post( event )
            

    def Notify(self, event):
        if isinstance( event, events.QuitEvent ):
            self.keepGoing = False
