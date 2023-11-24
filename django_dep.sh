#!/bin/bash
# Project specific environment vars
echo 'Intializing env vars...........'
db_host="hhcdjango.ctbmd1d7wwum.eu-north-1.rds.amazonaws.com"
db_port="5432"
db_name="hhcdb"
db_user="postgres"
db_pass="postgres123"
# emil app details
email='hhc4you@gmail.com'
email_app_key='ntudgjozyuznzyms'
#gdal environment veriable
CPLUS_INCLUDE_PATH=/usr/include/gdal
C_INCLUDE_PATH=/usr/include/gdal
# django super user details
DJANGO_SUPERUSER_PASSWORD=hhc4you
echo "Installing OS packages.."
sudo add-apt-repository -y ppa:ubuntugis/ppa 
sudo apt update -y
sudo apt install -y python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl postgis postgresql-14-postgis-3 python3-pip libgdal-dev gdal-bin
# git clone https://github.com/farsi8273/HHC_Trust_Deployment.git
# cd HHC_Trust_Deployment/

echo "Creating  python environment.........."
python3 -m venv hhcenv
source ./hhcenv/bin/activate
echo 'Installing required project dependencies.......'
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
gunicorn -c gunicorn.py
# chmod +x gunicorn_server.sh
# ./gunicorn_server.sh
# gunicorn \

#     --workers 2 \
#     --bind 0.0.0.0:8000 \
#     --log-level=info \
#     hhc.wsgi:application


