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
import graphicscontroller

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
    graphicscontroller.init()
    try:

        #
        # Build world
        #
        cfg = config.config
        pygame.mouse.set_visible(1)

        # load sprites, etc
        mech = mechsprite.Mech()
        
        em = eventmanager.evManager
        
        cpu = cpucontroller.CPUController()
        kyb = keyboardcontroller.KeyboardController()
        graphics = graphicscontroller.graphics
        
        graphics.AddSprite(mech)
        
        em.RegisterListener(cpu)
        em.RegisterListener(kyb)
        em.RegisterListener(graphics)
        
        cpu.Run()

    except:
        log.exception("Main loop caught fatal exception")
    finally:
        log.info("Finalizing...")
        pygame.quit()


# this should always be the last thing in the file
if __name__ == '__main__':
    main()
