"""
A test module containing all integration/functional tests
"""
import unittest
import webtest
import os

from pyramid.paster import get_appsettings

from scrooge_mcbot.server import main

# functional tests
class FunctionalTests(unittest.TestCase):
    """
    Functional/Integration tests for the main app
    """
    def setUp(self):
        """
        Get the app settings and use ``webtest.TestApp()`` to instantiate the test app
        """
        settings = get_appsettings('scrooge_mcbot'
                                   '/app_settings/pytest.ini')
        global_settings =  {
            '__file__': '{0}/scrooge_mcbot/app_settings/pytest.ini'.format(os.getcwd())
        }
        app = main(global_settings, **settings)
        self.testapp = webtest.TestApp(app)

    def test_root(self):
        """
        Test the GET request for the root directory
        """
        resp = self.testapp.get('/')
        self.assertEqual(resp.json_body, 'Hello message: Hello, there!')

    def test_home_post(self):
        """
        Test the POST request for the /home_post directory
        """
        resp = self.testapp.post_json('/home_post', params='testing...')
        self.assertEqual(resp.json_body['message'], 'You sent: testing...')
        self.assertIsInstance(resp.json_body['random_number'], int)
