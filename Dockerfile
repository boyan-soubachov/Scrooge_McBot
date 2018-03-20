FROM python:3

WORKDIR /usr/src/app
ADD . .

RUN pip install .

EXPOSE 8000

ENTRYPOINT ["scrooge_mcbot/bin/entrypoint.sh"]
