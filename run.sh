#!/bin/bash
echo "WebPhish Installer"

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


echo "installing pakeges for WebPhish"

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

export DJANGO_SUPERUSER_USERNAME=webphish
export DJANGO_SUPERUSER_PASSWORD=webphish
export DJANGO_SUPERUSER_EMAIL="webphish@webphish.com"
python manage.py createsuperuser --noinput
clear
cat << EOF

  888       888          888      8888888b.  888      d8b          888   V1.0
  888   o   888          888      888   Y88b 888      Y8P          888      
  888  d8b  888          888      888    888 888                   888      
  888 d888b 888  .d88b.  88888b.  888   d88P 88888b.  888 .d8888b  88888b.  
  888d88888b888 d8P  Y8b 888 "88b 8888888P"  888 "88b 888 88K      888 "88b 
  88888P Y88888 88888888 888  888 888        888  888 888 "Y8888b. 888  888 
  8888P   Y8888 Y8b.     888 d88P 888        888  888 888      X88 888  888 
  888P     Y888  "Y8888  88888P"  888        888  888 888  88888P' 888  888

  code by - Saurabh Wadekar[INDIA]

EOF

echo "Server Started"
echo "localhost : http://127.0.0.1:8080"
echo "admin : http://127.0.0.1:8080/admin"
echo "Defoult Username : webphish , Password : webphish"

python manage.py runserver 0.0.0.0:8080 &> /dev/null
