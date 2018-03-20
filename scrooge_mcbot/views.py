"""
This module contains all the views which map directly to the API routes.
"""
import logging
import random

import pyramid.response as pyramid_response
from pyramid.view import view_config
from scrooge_mcbot.controllers import dialogflow_controller

LOGGER = logging.getLogger()


@view_config(route_name='dialogflow', renderer='json')
def dialogflow_view(request):
    """
    TODO: add docs
    """
    request_body = request.swagger_data['body']
    action = request_body['result']['action']
    displayText, speech = getattr(dialogflow_controller, action)(6801015800084)
    LOGGER.info('request: %s', action)
    output = {
        "displayText": displayText,
        "speech": speech
    }
    resp = pyramid_response.Response(json_body=output)
    resp.status_code = 200
    return resp
