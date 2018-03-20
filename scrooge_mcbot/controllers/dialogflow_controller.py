"""
A controller module containing the business logic for any 'hello' endpoints.
"""
import logging

LOGGER = logging.getLogger()


def find_out_savings():
    """
    This is a simple controller endpoint.

    Returns:
        A simple, constant string message
    """
    response = 'You can save so much money with Scrooge McBot'
    LOGGER.info('Simple endpoint hit, response: %s', response)
    return response, response
