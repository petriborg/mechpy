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
except:
    log.exception("Unable to initialize game, missing modules")
    sys.exit(1)

#
# Load less important basics we don't expect to fail
#

import ConfigParser, shutil

#
# Main
#

def main():
    #
    # Load configuration
    #

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'data')
    user_dir = os.getenv("HOME")

    if os.name == 'posix':
        config_dir = os.path.join(user_dir, '.config')
        if not os.path.isdir(config_dir):
            config_dir = os.path.join(user_dir, '.local', 'Share')
            if not os.path.isdir(config_dir):
                log.info("Can't find ~/.config or ~/.local, not linux?")
                sys.exit(1)
    else:
        log.info("Not linux?")
        sys.exit(1)

    program_config_dir = os.path.join(config_dir, 'mechpy')
    program_config_file = os.path.join(program_config_dir, 'config.ini')

    if not os.path.exists(program_config_dir):
        log.info("Configuration directory did not exist, creating")
        os.mkdir(program_config_dir)

    if not os.path.exists(program_config_file):
        log.info("Configuration did not exist, copying over default")
        default_config_file = os.path.join(data_dir, 'default_config.ini')
        shutil.copyfile(default_config_file, program_config_file)

    config = ConfigParser.SafeConfigParser()
    config.read(program_config_file)

    pygame.init()
    try:
        clock = pygame.time.Clock()

        #
        # Build world
        #

        # TODO

        #
        # Main event loop
        #
        running = True
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT or \
                   event.type == KEYDOWN and event.key == K_ESCAPE:
                    going = False

                #
                # Handle inputs
                #

                # TODO

            #
            # Render
            #

            # TODO
    except:
        log.exception("Main loop caught fatal exception")
    finally:
        log.info("Finalizing...")
        pygame.quit()


if __name__ == '__main__':
    main()

