import os
from celery import Celery 

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')

#Used 'cel' instead of 'app', like in the documentation, to avoid any confusion since this project already has a module named 'app'.
cel = Celery('sample', 
             broker='redis://',
             backend='redis://',
             include=['sample.tasks'])

# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
cel.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
cel.autodiscover_tasks()

@cel.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')