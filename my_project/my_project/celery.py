#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


class Config:
    enable_utc = True

    timezone = 'Europe/Kiev'

    # REDIS related settings
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
    CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
    CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

app = Celery('my_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(Config, namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task
def add(x, y):
    print("Hello celery")
    return x + y
# celery sheduling
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html


app.conf.beat_schedule = {
    'add-every-5-min': {
        # 'task': 'my_project.celery.add',
        'task': 'news_scrap.tasks.blablabla',
        'schedule': crontab(minute='*/5'),
    },
}
