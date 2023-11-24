#!/bin/bash

# Gunicorn Config Script

# Define your application's module and callable
APP_MODULE="hhc.wsgi:application"

# Number of worker processes
WORKERS=2

# Bind address and port
BIND_ADDRESS="0.0.0.0"
BIND_PORT=8000

# Gunicorn log file
LOG_FILE= "gunicorn.log"

# PID file for Gunicorn process
PID_FILE="gunicorn.pid"

# Activate your virtual environment (if applicable)
# source /path/to/your/virtualenv/bin/activate
# mkdir -p /var/log/gunicorn/
# touch /var/log/gunicorn/dev.log
# Start Gunicorn
gunicorn \
    --workers $WORKERS \
    --bind $BIND_ADDRESS:$BIND_PORT \
    --log-level=info \
    --access-logfile=$LOG_FILE
    # --log-file=$LOG_FILE \
    # --pid=$PID_FILE \
    $APP_MODULE