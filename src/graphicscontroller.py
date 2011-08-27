"""
mechpy graphics controller
(this may be too general? consider further definition.)
"""

#
# Load logging
#
import logging, sys, os, util

log = logging.getLogger(__name__)

log.info("Loading Graphics Controller...")

import events
import pygame
import config

graphics = None

def init():
    """
    Initialize the singleton once in main
    """
    global graphics
    graphics = GraphicsController()

class GraphicsController:
    
    def __init__(self):
        self.name = "Graphics Controller"
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
            #
            # Render
            #
            self.allsprites.update()
            self.allsprites.draw(self.screen)
            pygame.display.flip()
        
    def AddSprite( self, sprite ):
        self.allsprites.add(sprite)
