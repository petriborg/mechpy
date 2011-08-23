"""
mechpy configuration, singleton,
ie:
>>> from config import config
>>> config.SCREEN_WIDTH
768
"""

#
# Import python system libraries
#
import os, sys, logging, ConfigParser, shutil

log = logging.getLogger(__name__)

#
# configuration singleton
#
config = None

def init():
    """
    Initialize the singleton once in main
    """
    global config
    config = Config()

#
# Helper functions for creating properties
# TODO move these into class Config
#

def _section_key_split(seckey):
    idx = seckey.index('.')
    section = seckey[0:idx]
    key = seckey[idx+1:]
    return (section, key)

def _str_property(seckey, docstr=None):
    (section, key) = _section_key_split(seckey)
    return property(
        lambda self: self._config.get(section, key),
        lambda self, x: self._config.set(section, key, x),
        None,
        docstr)

def _bool_property(seckey, docstr=None):
    (section, key) = _section_key_split(seckey)
    return property(
        lambda self: self._config.getboolean(section, key),
        lambda self, x: self._config.set(section, key, x),
        None,
        docstr)

def _int_property(seckey, docstr=None):
    (section, key) = _section_key_split(seckey)
    return property(
        lambda self: self._config.getint(section, key),
        lambda self, x: self._config.set(section, key, x),
        None,
        docstr)

def _float_property(seckey, docstr=None):
    (section, key) = _section_key_split(seckey)
    return property(
        lambda self: self._config.getfloat(section, key),
        lambda self, x: self._config.set(section, key, x),
        None,
        docstr)



#
# list of properties attached to the configuration properties file
#
class Config:

    #
    # List of all configuration properties
    #

    SCREEN_WIDTH = _int_property("gfx.screen_width",
        """Width of the display screen""")
    SCREEN_HEIGHT = _int_property("gfx.screen_height",
        """Height of the display screen""")

    def __init__(self):
        """
        Call this function whenever you want the configuration to be
        initialized, should be called in main().
        """
        global _config

        #
        # Load configuration
        #
        src_dir = os.path.split(os.path.abspath(__file__))[0]
        main_dir = os.path.abspath(os.path.join(src_dir, '..'))
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
            default_config_file = os.path.join(data_dir, 
                                               'default_config.ini')
            shutil.copyfile(default_config_file, program_config_file)

        self._config = ConfigParser.SafeConfigParser()
        self._config.read(program_config_file)


