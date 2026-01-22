#!/bin/bash
python DjangoSocial/manage.py collectstatic --noinput
python DjangoSocial/manage.py migrate
gunicorn DjangoSocial.DjangoSocial.wsgi:application --bind 0.0.0.0:$PORT
