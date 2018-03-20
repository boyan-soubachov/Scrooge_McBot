"""
All Pyramid middleware (tweens and other hooks) live here and are implicitly called in the
relevant config .ini file.
"""
import datetime
import decimal
import logging

from pyramid.renderers import JSON

LOGGER = logging.getLogger()


def add_custom_adapters(config):
    """
    Adds custom adapters to the Pyramid JSON renderer. Used to convert objects to JSON-compatible
    ones, e.g. Decimal -> float
    Args:
        config(object): A Pyramid config object, according to pyramid spec.
    """
    json_renderer = JSON()
    json_renderer.add_adapter(decimal.Decimal, _convert_decimal)
    json_renderer.add_adapter(datetime.datetime, _convert_datetime)
    config.add_renderer('json', json_renderer)


def _convert_decimal(object, request):
    return float(object)


def _convert_datetime(object, request):
    return object.isoformat() + 'Z'


def remove_nones_from_dict(handler, registry):
    """
    A tween that removes Nones (i.e. nulls) recursively in the response dictionary. This eliminates
    the need to explicitly handle them in the views.
    Args:
        handler(object): A function that runs the view handler registered with Pyramid for the
        request.
        registry(object): The Pyramid config/settings registry.
    Returns:
        A function that will be called in the processing chain (this is the tween).
    """
    def _clear_nones_from_dict(request):
        response = handler(request)

        def loop_dict(input_dict):
            """
            Recursively loops through the input dictionary and removes all Nones.
            """
            res_dict = {}
            for k, v in input_dict.items():
                if v is None:
                    continue
                if isinstance(v, dict):
                    res_dict[k] = loop_dict(v)
                if isinstance(v, list):
                    res_dict[k] = loop_list(v)
                res_dict[k] = v
            return res_dict

        def loop_list(input_list):
            """
            Recursively loops through the input list and removes all Nones.
            """
            res_list = []
            for item in input_list:
                if isinstance(item, dict):
                    res_list.append(loop_dict(item))
                elif isinstance(item, list):
                    res_list.append(loop_list(item))
                else:
                    res_list.append(item)
            return res_list
        # Pass-through requests without a body
        if not response.body:
            return response
        if isinstance(response.json_body, dict):
            response.json_body = loop_dict(response.json_body)
        elif isinstance(response.json_body, list):
            response.json_body = loop_list(response.json_body)
        return response
    return _clear_nones_from_dict
