"""
mechpy gui controller
"""

#
# Load logging
#
import logging, sys, os, util

log = logging.getLogger(__name__)

log.info("Loading GUI Controller...")

import events
import pygame
import config

gui = None

def init():
    """
    Initialize the singleton once in main
    """
    global gui
    gui = GUIController()

class GUIController:
    
    def __init__(self):
        self.name = "GUI Controller"
        cfg = config.config
        self.screen = pygame.display.set_mode(
                    (cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
        # render initial load screen
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        self.screen.blit(background, (0,0))
        pygame.display.flip()
        self.allsprites = pygame.sprite.RenderPlain([])
        
    def Notify(self, event):
        if isinstance( event, events.TickEvent ):
			# Let sprites do their stuff
			self.allsprites.update()
			# Render
			self.allsprites.draw(self.screen)
			pygame.display.flip()
        
    def AddSprite( self, sprite ):
        self.allsprites.add(sprite)
