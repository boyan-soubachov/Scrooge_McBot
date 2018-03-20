"""
A controller module containing the business logic for any 'hello' endpoints.
"""
import logging

LOGGER = logging.getLogger()


def get_hello_message():
    """
    This is a simple controller endpoint.

    Returns:
        A simple, constant string message
    """
    response = 'Hello, there!'
    LOGGER.info('Simple endpoint hit, response: %s', response)
    return response

def echo_hello_message(hello_message):
    """
    An echo-ing controller (business logic).

    Args:
        hello_message (string): A string input to echo.
    Returns:
        A simple string which echoes the input.
    """
    response = "You sent: {0}".format(hello_message)
    LOGGER.info('Echo response: %s', response)
    return response
