from multiprocessing import cpu_count
from os import environ

def max_workers():
    return cpu_count()

daemon = False
bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000
worker_class = 'gevent'
workers = 4 # ( max_workers() * 2 ) + 1 
timeout = 60
accesslog="access.log"
errlog="err.log"
# threads = 2

