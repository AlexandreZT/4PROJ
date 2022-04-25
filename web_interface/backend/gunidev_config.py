"""gunicorn server configuration."""
threads = 2
workers = 2
timeout = 360
bind = "127.0.0.1:5000"
certfile = './cert.pem'
keyfile = './key.pem'
reload = True
# worker_class = "uvicorn.workers.UvicornWorker"
