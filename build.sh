#!/bin/bash
# Install dependencies
pip install -r requirements.txt
# collect static files
python manage.py collectstatic --noinput
# Run migrations
python manage.py clear_cache
python manage.py makemigrations
python manage.py migrate 