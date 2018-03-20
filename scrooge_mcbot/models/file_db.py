import os

import logging


def _get_file_lines():
    return [line.strip('\n') for line in open('file_db', 'r')]


def get_policyholder_id(id_number):
    logging.info(_get_file_lines())
    for line in _get_file_lines():
        splits = line.split(';')
        if splits[0] == str(id_number):
            return splits[1]
