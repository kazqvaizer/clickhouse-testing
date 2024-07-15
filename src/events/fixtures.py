from typing import TYPE_CHECKING

import pytest

from events.models import Event

if TYPE_CHECKING:
    from app.testing.factory import FixtureFactory


@pytest.fixture
def event(factory: "FixtureFactory") -> Event:
    return factory.event()
