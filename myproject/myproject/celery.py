# from __future__ import absolute_import
# import os
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
#
# app = Celery('myproject')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

#New2
from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'create-nugget-every-day': {
        'task': 'your_app.tasks.create_nugget_task',
        'schedule': crontab(hour=0, minute=5),
        'args': ('Sample content',),
    },
}
