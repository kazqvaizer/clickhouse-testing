from uuid import uuid4

from app.celery import celery
from events.models import Event


@celery.task(name="create_events")
def create_events() -> None:
    Event.objects.create(payload=str(uuid4()))
