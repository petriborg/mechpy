"""
mechpy battle controller
"""

#
# Load logging
#
import logging, sys, os, util

log = logging.getLogger(__name__)

log.info("Loading Battle Controller...")

import events
import pygame
import config

battle = None

def init():
    """
    Initialize the singleton once in main
    """
    global battle
    battle = BattleController()

class BattleController:
    
    BATTLESTOPPED = 0
    BATTLERUNNING = 1
    BATTLEPAUSED = 2
    
    def __init__(self):
        self.name = "Battle Controller"
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
        self.state = BattleController.BATTLESTOPPED
        
    def Start(self):
        self.state = BattleController.BATTLERUNNING
        
    def Stop(self):
        self.state = BattleController.BATTLESTOPPED
        
    def Pause(self):
		self.state = BATTLEPAUSED
        
    def Notify(self, event):
        if isinstance( event, events.TickEvent ):
            if self.state == BattleController.BATTLERUNNING:
                # Let sprites do their stuff
                self.allsprites.update()
                # Render
                self.allsprites.draw(self.screen)
                pygame.display.flip()
        
    def AddSprite( self, sprite ):
        self.allsprites.add(sprite)
