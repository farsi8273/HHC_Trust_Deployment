import multiprocessing

bind = "0.0.0.0:8000" 
# bind = "gunicorn-socket.sock" 
## Change the host and port as needed
workers = multiprocessing.cpu_count() * 2 + 1  # Adjust the number of workers based on your system
errorlog = "/home/ubuntu/gunicorn_error.log" # Specify the path to the error log
accesslog = "/home/ubuntu/gunicorn_access.log"
loglevel = "info"  # Adjust the log level: debug, info, warning, error, critical
timeout = 120  # Set the timeout for worker processes in seconds
max_requests = 1000  # Set the maximum number of requests a worker will process before restarting

# If using a virtual environment, specify its path
# pythonpath = '/path/to/your/virtualenv'

# If using a Django application, specify the location of the WSGI module
wsgi_app = 'hhc.wsgi:application'
