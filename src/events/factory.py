from app.testing import register
from app.testing.types import FactoryProtocol
from events.models import Event


@register
def event(self: FactoryProtocol, **kwargs: dict) -> Event:
    return self.mixer.blend("events.Event", **kwargs)
