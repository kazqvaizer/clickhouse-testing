import os
from datetime import timedelta

from celery import Celery
from celery.schedules import schedule
from django.conf import settings

__all__ = ["celery"]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

celery = Celery("app")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

celery.conf.beat_schedule = {
    "create_events": {
        "task": "create_events",
        "schedule": schedule(run_every=timedelta(seconds=5)),
        "options": {
            "expires": 3 * 60,
        },
    },
}
