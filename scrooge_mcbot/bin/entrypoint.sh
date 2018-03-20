#!/bin/bash

exec gunicorn --bind 0.0.0.0:8000 \
--paste scrooge_mcbot/app_settings/production.ini \
--name scrooge_mcbot \
--workers 4 \
--log-level=info \
--log-file=/var/log/gunicorn.log \
--access-logfile=/var/log/gunicorn-access.log
