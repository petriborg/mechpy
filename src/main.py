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
# Main
#
def main():
    config.init() # load configuration
    pygame.init()
    try:
        clock = pygame.time.Clock()

        #
        # Build world
        #
        cfg = config.config
        screen = pygame.display.set_mode(
                    (cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
        pygame.mouse.set_visible(0)

        # render initial load screen
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        screen.blit(background, (0,0))
        pygame.display.flip()

        # load sprites, etc
        # TODO
        allsprites = pygame.sprite.RenderPlain([])

        #
        # Main event loop
        #
        running = True
        while running:
            clock.tick(30)
            
            if not ControllerTick():
                running = False

            ViewTick()

    except:
        log.exception("Main loop caught fatal exception")
    finally:
        log.info("Finalizing...")
        pygame.quit()


def ControllerTick():
    for event in pygame.event.get():
        if event.type == QUIT or \
           event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

        #
        # Handle inputs
        #

        # TODO

def ViewTick():
    #
    # Render
    #
    allsprites.update()
    allsprites.draw(screen)
    pygame.display.flip()


# this should always be the last thing in the file
if __name__ == '__main__':
    main()
