"""
This module contains all the views which map directly to the API routes.
"""
import logging
import random

import pyramid.response as pyramid_response
from pyramid.view import view_config
from scrooge_mcbot.controllers import hello_controller

LOGGER = logging.getLogger()

@view_config(route_name='home', renderer='json')
def my_view(request):
    """
    View for the simple, 'home' request route.

    Args:
        request (object): An object containing request data.
    """
    controller_data = hello_controller.get_hello_message()
    
    resp = pyramid_response.Response(
        json_body='Hello message: {0}'.format(controller_data)
    )
    resp.status_code = 200
    return resp

@view_config(route_name='home_post', renderer='json')
def home_post_view(request):
    """
    View for the more complex, 'home_post' request route.

    Args:
        request (object): An object containing request data.
    """
    request_body = request.swagger_data['body']
    LOGGER.info('Request body: %s', request_body)
    processed_data = hello_controller.echo_hello_message(request_body)
    output = {
        'message': processed_data,
        'random_number': random.randint(1, 8)
    }
    resp = pyramid_response.Response(json_body=output)
    resp.status_code = 201
    return resp
