import pytest

from events.models import Event

pytestmark = [pytest.mark.django_db(databases=["default", "clickhouse"])]


def test_create_event():

    assert Event.objects.count() == 0

    Event.objects.create()

    assert Event.objects.count() == 1


def test_update_event(event):
    event.payload = "hey!"
    event.save(update_fields=["payload"])

    event.refresh_from_db()

    assert event.payload == "hey!"


def test_delete_event(event):
    event.delete()

    assert Event.objects.count() == 0
