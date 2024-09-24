import os
from celery import Celery 

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')

cel = Celery('sample')

# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
cel.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
cel.autodiscover_tasks()

@cel.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')