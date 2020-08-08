from __future__ import absolute_import, unicode_literals
import os, environ, sys

from celery import Celery

from shopping.settings.base import BASE_DIR

env = environ.Env()
env.read_env('settings.env')

app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, 'shopping'))

# select settings file to be used
os.environ.setdefault(env('DJANGO_SETTINGS_MODULE'), 'shopping.settings.development')

app = Celery('shopping')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
