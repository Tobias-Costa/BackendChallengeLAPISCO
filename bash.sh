#!/bin/bash

echo "Create migrations"
python manage.py makemigration library_api
echo "===================================="

echo "Migrate"
python manage.py migrate
echo "===================================="

echo "Start server"
python manage.py runserver 0.0.0.0:8000