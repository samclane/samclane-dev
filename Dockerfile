FROM python:3.8.1-slim-buster

MAINTAINER Sawyer McLane "sawyer@protonmail.com"

ENV HOME=/home
ENV APP_HOME=/home/flask_app

COPY ./flask_app/requirements.txt /home/flask_app/requirements.txt

WORKDIR /home/flask_app

RUN pip install -r requirements.txt

COPY . /home/flask_app

COPY ./config/config.json /etc/config.json

WORKDIR /home/flask_app

ENTRYPOINT [ "gunicorn" ]

CMD [ "--bind", "0.0.0.0:5000", "flask_app:app" ]
