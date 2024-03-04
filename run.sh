#!/bin/bash
echo "WebPhish Installer"

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


echo "installing pakeges for WwbPhish"

# this script tested only garuda linux

pacman -S python-virtualenv
virtualenv venv
source ./venv/bin/activate || source ./venv/bin/activate.fish

if [ pip ]
then 
pip install -r requirements.txt


elif [ pip3 ]
then 
pip3 install -r requirements.txt

else echo "pip and pip3 not installed"
fi

clear
python manage.py makemigrations
python manage.py migrate
clear
echo "WebPhish 1.0"
echo "code by - Saurabh Wadekar"
echo "Starting..."
export DJANGO_SUPERUSER_USERNAME=webphish
export DJANGO_SUPERUSER_PASSWORD=webphish
export DJANGO_SUPERUSER_EMAIL="webphish@webphish.com"
python manage.py createsuperuser --noinput
python manage.py runserver