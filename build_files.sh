#!/bin/bash


# Install dependencies
pip3 install -r requirements.txt

export DJANGO_SETTINGS_MODULE=cotProject.settings

# Collect static files
python3 manage.py collectstatic --noinput --settings=SITechnicalChallenge.settings

# Collect static files
python3 manage.py collectstatic --noinput

# Copy media files
cp -R media staticfiles_build/media

