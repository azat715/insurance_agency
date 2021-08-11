#!/bin/sh

echo "Apply database migrations"
python manage.py migrate

echo "Loading fixture"
python manage.py loaddata fixture/test_case.json

echo "Starting server"
/code/wait-for-it.sh rabbitmq:5672 -- echo "run rabbitmq"
/code/wait-for-it.sh redis:6379 -- echo "run redis"
python manage.py runserver 0.0.0.0:8000

exec "$@"
