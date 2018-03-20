"""
The setup file defining parameters for the setuptools package/distribution builder.
Add any and all requirements here.
"""
import os

from setuptools import setup, find_packages

requires = [
    'gunicorn',
    'honeybadger',
    'jsonschema[format]',
    'pyramid',
    'pyramid_swagger',
    'waitress',
]

tests_require = [
    'tox',
    'webtest'
]

setup(
    name='scrooge_mcbot',
    version='0.0.0',
    description='Scrooge McBot',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Bob S',
    author_email='ununoctium87@gmail.com',
    url='',
    keywords='web pyramid pylons docker swagger',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = scrooge_mcbot.server:main',
        ],
    },
)
