import os
from django.utils import timezone
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


class MyAppCelery(Celery):
    def now(self):
        """Return the current time and date as a datetime."""
        return timezone.now()


app = MyAppCelery()
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
