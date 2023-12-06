#!/bin/bash
# Project specific environment vars
echo "creating databae"
sudo -u postgres psql
CREATE DATABASE hhcdb;
echo 'Intializing env vars...........'
source ./env.sh
echo "Installing OS packages......"
sudo add-apt-repository -y ppa:ubuntugis/ppa 
sudo apt update -y
sudo apt install -y python3-venv python3-dev libpq-dev postgresql postgresql-contrib curl postgis postgresql-14-postgis-3 python3-pip libgdal-dev gdal-bin
# git clone https://github.com/farsi8273/HHC_Trust_Deployment.git
# cd HHC_Trust_Deployment/

echo "Creating  Python environment.........."
python3 -m venv hhcenv
source ./hhcenv/bin/activate
echo 'Installing required project dependencies.......'
pip install -r requirements.txt
echo "running python project....."
python3 manage.py makemigrations
echo 'creating migration...........'
python3 manage.py migrate
echo ' migrate command in completed.............'
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
echo 'Before collectstatic...........'
python3 manage.py collectstatic --noinput
echo 'collectstatic completed successfully.....'
sudo ufw allow 8000
echo "Creating gunicorn Service file...."
sudo cp gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
# Nginx installation and configuration
sudo apt install -y nginx
public_ip=$(curl -s ifconfig.me)
echo "getting public ip.........: $(public_ip)"
sed -i "s/server_name.*/server_name $public_ip;/" ./hhc-server.conf
sudo cp hhc-server.conf /etc/nginx/sites-available/hhcproject
sudo ln -s /etc/nginx/sites-available/hhcproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw allow 'Nginx Full'
sudo cp myscript.service /etc/systemd/system/myscript.service
sudo systemctl enable myscript


