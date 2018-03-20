"""
Utilities used for bringing up the Pyramid service correctly and as intended.
"""
import logging
import yaml

LOGGER = logging.getLogger()

def register_routes_from_swagger(config):
    """
    Parses a Swagger yaml file for route specification and configures all routes
    onto the Pyramid server.

    Args:
        config (object): A Pyramid Configuration object which has loaded the relevant
        Swagger file.
    """
    settings = config.get_settings()
    # Append trailing slash if not present
    if settings['pyramid_swagger.schema_directory'][-1] != '/':
        settings['pyramid_swagger.schema_directory'] += '/'
    swagger_spec_path = "{0}{1}".format(
        settings['pyramid_swagger.schema_directory'],
        settings['pyramid_swagger.schema_file']
    )
    with open(swagger_spec_path) as phile:
        yaml_dict = yaml.load(phile)
        base_path = '' if yaml_dict['basePath'] == '/' else yaml_dict['basePath']
        for k, v in yaml_dict['paths'].items():
            pattern = "{base}{path}".format(base=base_path, path=k)
            for verb, data in v.items():
                route_name = data['operationId']
                LOGGER.info(
                    'Adding Swagger route name=%s, method=%s, pattern=%s',
                    route_name,
                    verb.upper(),
                    pattern
                )
                config.add_route(name=route_name, pattern=pattern, request_method=verb.upper())
