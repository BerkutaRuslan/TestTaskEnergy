from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import celery
from celery import shared_task

# set the default Django settings module for the 'celery' program.
from ukr_project import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ukr_project.settings')

app = Celery('ukr_project',)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(CELERY_REDIS_MAX_CONNECTIONS=10,)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
