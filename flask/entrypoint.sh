#!/bin/sh

# Create passwords file if not found
# python seed_script.py

# Serve flask application using uwsgi
uwsgi --ini /etc/uwsgi.ini --chdir /var/www/flask
