"""
mechpy main function
"""

#
# Load logging
#
import logging, sys, os

logging_stream = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

#
# Load main modules, pygame, etc
#
log.info("Starting...")
try:
    # Load all the system modules here that might not properly exist
    # as part of the default python install to ensure they are properly
    # installed onto the system already.
    import pygame
    from pygame.locals import *
except:
    log.exception("Unable to initialize game, missing modules")
    sys.exit(1)

#
# Load less important basics we don't expect to fail
#
import config

#
# Load sprites
import mechsprite

#
# Load controllers
import cpucontroller
import keyboardcontroller
import cursorcontroller
import battlecontroller
#import guicontroller

#
# Load eventmanager
import eventmanager

#
# Main
#
def main():
    config.init() # load configuration
    pygame.init()
    eventmanager.init()
    battlecontroller.init()
    #guicontroller.init()
    try:

        #
        # Build world
        #
        cfg = config.config
        pygame.mouse.set_visible(1)
        
        em = eventmanager.evManager
        
        cpu = cpucontroller.CPUController()
        kyb = keyboardcontroller.KeyboardController()
        cur = cursorcontroller.CursorController()
        bat = battlecontroller.battle
        #gui = guicontroller.gui
        
        #testing
        mech = mechsprite.Mech()
        bat.AddSprite(mech)
        bat.Start()
        
        em.RegisterListener(cpu)
        em.RegisterListener(kyb)
        em.RegisterListener(cur)
        em.RegisterListener(bat)
        #em.RegisterListener(gui)
        
        cpu.Run()

    except:
        log.exception("Main loop caught fatal exception")
    finally:
        log.info("Finalizing...")
        pygame.quit()


# this should always be the last thing in the file
if __name__ == '__main__':
    main()
