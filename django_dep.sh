#!/bin/bash
echo "Installing OS packages.."
sudo add-apt-repository -y ppa:ubuntugis/ppa 
sudo apt update -y
sudo apt install -y python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl postgis postgresql-14-postgis-3 python3-pip libgdal-dev gdal-bin
# git clone https://github.com/farsi8273/HHC_Trust_Deployment.git
# cd HHC_Trust_Deployment/
echo 'Intializing env vars...........'
sh ./env.sh
echo "Creating  python environment.........."
python3 -m venv hhcenv
source ./hhcenv/bin/activate
echo 'Installing required project dependencies.......'
pip install -r requirements.txt
echo "running python project.."
python3 manage.py makemigrations
python3 manage.py migrate
USERNAME="admin"
EMAIL="hhc4you@gmail.com"
# Check if the superuser already exists
existing_superuser=$(python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='$USERNAME').exists())")

if [ "$existing_superuser" = "False" ]; then
    # Create the superuser
    python manage.py createsuperuser --username=$USERNAME --email=$EMAIL --noinput
    echo "Superuser created successfully."
else
    echo "Superuser '$USERNAME' already exists."
fi
# python3 manage.py createsuperuser --noinput --username admin --email $email
python3 manage.py collectstatic --noinput
sudo ufw allow 8000
gunicorn -c gunicorn.conf

