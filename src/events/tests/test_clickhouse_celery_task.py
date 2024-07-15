import pytest

from events.models import Event
from events.tasks import create_events

pytestmark = [pytest.mark.django_db(databases=["default", "clickhouse"])]


def test_create_event_via_task():

    assert Event.objects.count() == 0

    create_events()

    assert Event.objects.count() == 1
