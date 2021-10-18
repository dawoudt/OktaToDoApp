#!/bin/bash

set -e

# assert python version greater than 3.8

echo "Requires python version 3.8+"
echo "Your python version: $(python --version)"

BASE_PATH=$(pwd)
BACKEND=$BASE_PATH/backend
FRONTEND=$BASE_PATH/frontend

echo "Copying .env file"
cp .env.example .env

set -o allexport
source .env
set +o allexport

cp .env $FRONTEND/.env


python -m venv $BACKEND/.venv;
echo "Python virtual env created successfully"

source $BACKEND/.venv/bin/activate
echo "entering virtual env"
echo "Installing requirements"

python -m pip install -r $BACKEND/requirements.txt

echo "running migrations"
python $BACKEND/manage.py makemigrations
python $BACKEND/manage.py migrate

echo "Done..."
echo "Running backend on localhost"

python $BACKEND/manage.py runserver


