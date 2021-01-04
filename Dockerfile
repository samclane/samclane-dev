FROM ubuntu:16.04

MAINTAINER Sawyer McLane "sawyer@protonmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./flask_app/requirements.txt /flask_app/requirements.txt

WORKDIR /flask_app

RUN pip install -r requirements.txt

COPY ./flask_app /flask_app

COPY ./config/config.json /etc/config.json

ENV FLASK_APP=.

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host", "0.0.0.0" ]
