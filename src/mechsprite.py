"""
mechpy mech sprite
"""

#
# Load logging
#
import logging, sys, os, util

log = logging.getLogger(__name__)

log.info("Loading Mech Sprite...")

import config
import pygame
from pygame.locals import *

class Mech(pygame.sprite.Sprite):
    """The Mech class, for representing mechs"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        cfg = config.config
        self.image, self.rect = util.load_image('small/wheelchassis.png', -1)
        #self.rect.center. = cfg.SCREEN_WIDTH/2
        #self.rect.mid = pos
        self.armor = None
        self.chassis = None
        self.cpu = None
        self.power = None
        self.targetingAI = None
        self.movementAI = None
        self.weaponAI = None
        self.specialAI = None

    def update(self):
        "move the mech based on the movementAI"
        #pos = self.movementAI.getNextPos()
