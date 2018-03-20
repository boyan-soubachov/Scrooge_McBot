"""
A test module containing all tests related to the controllers
"""
import unittest

from scrooge_mcbot.controllers import hello_controller

# controller tests
class ControllerTests(unittest.TestCase):
    """
    The unit tests for the controller methods
    """
    def test_get_hello_message(self):
        """
        A unit test for ``get_hello_message()``
        """
        # get response from get_hello_message()
        res = hello_controller.get_hello_message()
        self.assertEqual(res, 'Hello, there!')

    def test_echo_hello_message(self):
        """
        A unit test for ``echo_hello_message()
        """
        test_str = 'Test String'
        # resp from echo_hello_message()
        res = hello_controller.echo_hello_message(test_str)
        self.assertEqual(res, 'You sent: {0}'.format(test_str))
