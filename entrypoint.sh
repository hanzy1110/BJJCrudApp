#!/bin/sh
echo "Entrypoint..."
# source .env.prod
echo "Setting up database..."
python manage.py makemigrations
python manage.py migrate BJJCrudApp
python manage.py collectstatic --noinput
# python manage.py createsuperuser --no-input

sleep 10
echo "Starting Server..."

# python manage.py runserver 0.0.0.0:${WEB_PORT}
