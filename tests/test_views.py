"""
A test module containing all tests related to the controllers
"""
import unittest

from pyramid import testing

from scrooge_mcbot import views

# view tests
class ViewTests(unittest.TestCase):
    """
    The unit tests for the views methods
    """
    def setUp(self):
        """
        Get config from ``pyramid.testing.setUp()``
        """
        self.config = testing.setUp()

    def tearDown(self):
        """
        Get config from ``pyramid.testing.setUp()``
        """
        testing.tearDown()

    def test_my_view(self):
        """
        A unit test for ``test_my_view()```
        """
        request = testing.DummyRequest()
        info = views.my_view(request)
        hello_msg = 'Hello, there!'
        self.assertEqual(info.json_body, 'Hello message: {0}'.format(hello_msg))

    def test_home_post_view(self):
        """
        A unit test for ``test_home_post_view()```
        """
        req = DummyRequest()
        info = views.home_post_view(req)
        self.assertEqual(info.json_body['message'], 'You sent: {0}'.format('testing...'))


# add swagger_data attribute to DummyRequest class
class DummyRequest(testing.DummyRequest):
    """
    Adds a ``swagger_data`` attribute to ``testing.DummyRequest``

    Inherits from: ``testing.DummyRequest``
    """
    swagger_data = {'body': 'testing...'}
