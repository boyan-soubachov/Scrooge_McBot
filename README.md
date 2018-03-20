# Scrooge McBot

## About

TODO: This is descriptive information about your newly-created API. Please enter a brief description of what its functionality is, how to get it up and running and how to modify it.

NB: Assume that this code will be maintained by everyone and not just your team. Make sure you're descriptive and provide good guidelines on how to maintain code quality.

## TL;DR

To get this service up and running quickly on your machine:

1. Change directory into your newly created project.

    ```cd scrooge_mcbot```

1. Create a Python virtual environment and activate it.

    ```bash

    virtualenv venv
    source venv/bin/activate

    ```

1. Install the package and all of its requirements.

    ```pip install -e .```

1. Run the server

    ```pserve scrooge_mcbot/app_settings/development.ini --reload```
    the server will then come up on port 8000

## Run tests

1. Install the package in editable mode with its testing requirements.

    ```pip install -e ".[testing]"```

1. Then just run `tox` from anywhere in the repo.
