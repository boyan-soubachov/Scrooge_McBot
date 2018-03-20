"""
A simple wrapper for loading and parsing the Pyramid configuration file to allow support for
non-Pyramid sections.
"""
import logging
from configparser import ConfigParser

LOGGER = logging.getLogger()
CONFIG = None
DEFAULTS = {

}


class PyramidConfig(object):
    """
    A simple Pyramid configuration class which thinly wraps Python's ConfigParser.
    """
    def __init__(self, config_file_path):
        LOGGER.info('Loading Pyramid config at: %s', config_file_path)
        self.parser = ConfigParser(defaults=DEFAULTS)
        found = self.parser.read(config_file_path)
        if not found:
            raise ValueError('Specified config file not found!, %s', config_file_path)

    def get_parser(self):
        """
        Returns the ConfigParser object.

        Returns:
            object: The configparser object or None if no config has been loaded.
        """
        return self.parser

def load_config(config_file_path):
    """
    Loads the specified config file and sets it as the global object `CONFIG`.

    Args:
        config_file_path (string): The full path to the desired config (ini) file.
    """
    global CONFIG
    if not isinstance(CONFIG, PyramidConfig):
        CONFIG = PyramidConfig(config_file_path=config_file_path).get_parser()

def get_config():
    """
    Returns the config object which has been loaded (ConfigParser type).
    """
    return CONFIG
