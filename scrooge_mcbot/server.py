"""
The main server module. Serves as the entry point (the main function) for the
WSGI-compatible server.
"""
import logging

from pyramid.config import Configurator
from scrooge_mcbot.utils import (pyramid_config, pyramid_utils,
                                              tweens)

LOGGER = logging.getLogger()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings_path = global_config['__file__']
    pyramid_config.load_config(settings_path)
    config = Configurator(settings=settings)
    tweens.add_custom_adapters(config)
    pyramid_utils.register_routes_from_swagger(config)
    config.scan()
    return config.make_wsgi_app()
