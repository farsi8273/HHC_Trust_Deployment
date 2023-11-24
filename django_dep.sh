#!/bin/bash
# Project specific environment vars
echo 'Intializing env vars...........'
sudo export db_host="hhcdjango.ctbmd1d7wwum.eu-north-1.rds.amazonaws.com"
sudo export db_port="5432"
sudo export db_name="hhcdb"
sudo export db_user="postgres"
sudo export db_pass="postgres123"
# emil app details
sudo export email='hhc4you@gmail.com'
sudo export email_app_key='ntudgjozyuznzyms'
#gdal environment veriable
sudo export CPLUS_INCLUDE_PATH=/usr/include/gdal
sudo export C_INCLUDE_PATH=/usr/include/gdal
# django super user details
sudo export DJANGO_SUPERUSER_PASSWORD=hhc4you
echo "Installing OS packages.."
sudo add-apt-repository -y ppa:ubuntugis/ppa 
sudo apt update -y
sudo apt install -y python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl postgis postgresql-14-postgis-3 python3-pip libgdal-dev gdal-bin
# git clone https://github.com/farsi8273/HHC_Trust_Deployment.git
# cd HHC_Trust_Deployment/

echo "Creating  python environment.........."
python3 -m venv hhcenv
source ./hhcenv/bin/activate
echo 'Installing required psudo roject dependencies.......'
pip install -r requirements.txt
echo "running python project.."
python3 manage.py makemigrations
echo 'creating migration............'
python3 manage.py migrate
echo ' migrate done.............'
USERNAME="admin"
EMAIL="hhc4you@gmail.com"
# Check if the superuser already exists
existing_superuser=$(python3 manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='$USERNAME').exists())")

if [ "$existing_superuser" = "False" ]; then
    # Create the superuser
    python3 manage.py createsuperuser --username=$USERNAME --email=$EMAIL --noinput
    echo "Superuser created successfully."
else
    echo "Superuser '$USERNAME' already exists."
fi
# python3 manage.py createsuperuser --noinput --username admin --email $email
echo 'before collectstatic...........'
python3 manage.py collectstatic --noinput
echo ' creating statics............'
sudo ufw allow 8000
sudo gunicorn -c gunicorn_conf.py
# chmod +x gunicorn_server.sh
# ./gunicorn_server.sh
# gunicorn \

#     --workers 2 \
#     --bind 0.0.0.0:8000 \
#     --log-level=info \
#     hhc.wsgi:application


