#!/bin/bash
ENV_NAME="gregazevedo"


unset PYTHONDONTWRITEBYTECODE
source `which virtualenvwrapper.sh`


workon $ENV_NAME
heroku buildpacks:add heroku/nodejs -a $ENV_NAME
heroku buildpacks:add heroku/python -a $ENV_NAME

heroku addons:create heroku-redis:hobby-dev --app $ENV_NAME

heroku config:set PYTHONHASHSEED=random --app $ENV_NAME
heroku config:set AWS_SECRET_ACCESS_KEY="" --app $ENV_NAME
heroku config:set AWS_ACCESS_KEY_ID="" --app $ENV_NAME
heroku config:set AWS_STORAGE_BUCKET_NAME=$ENV_NAME --app $ENV_NAME
heroku config:set SECRET_KEY=`python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'` --app $ENV_NAME
heroku config:set DJANGO_SETTINGS_MODULE=$ENV_NAME.$ENV_NAME.settings.heroku --app $ENV_NAME

git push heroku master
heroku run python manage.py migrate --app $ENV_NAME

echo "python manage.py migrate --noinput" >> bin/post_compile
