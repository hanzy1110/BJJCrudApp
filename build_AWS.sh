#!/bin/bash
# rm ./event_manager/migrations/*
set -xe
echo "Working dir"

APP_NAME="BJJCrudAPP"
sudo docker-compose --env-file envfiles/.env down --remove-orphans
sudo docker-compose --env-file envfiles/.env build --progress plain

echo MAKING AND APPLYING MIGRATIONS...
sudo docker-compose --env-file envfiles/.env run --rm bjjcrudapp bash -c "python manage.py makemigrations ${APP_NAME} && python manage.py migrate"
# sudo docker-compose --env-file .env run --rm crm_api sh -c "python manage.py migrate"

sudo docker-compose --env-file envfiles/.env up -d

echo "----------------------<>-----------------------"
echo Waiting for containers...
sleep 10
sudo docker ps -a

echo "----------------------<>-----------------------"
sudo docker logs -t --follow bjjcrudapp

# sudo docker exec -it crm_api bash
