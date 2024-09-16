#!/bin/bash


# Install dependencies
pip3 install -r requirements.txt

export DJANGO_SETTINGS_MODULE=SITechnicalChallenge.settings

# Collect static files
python3 manage.py collectstatic --noinput --settings=SITechnicalChallenge.settings

# Collect static files
python3 manage.py collectstatic --noinput


