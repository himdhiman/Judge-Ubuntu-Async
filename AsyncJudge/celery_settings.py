import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsyncJudge.settings')

app = Celery('AsyncJudge')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()