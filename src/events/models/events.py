from clickhouse_backend import models as ch_models
from django.utils import timezone


class Event(ch_models.ClickhouseModel):

    event = ch_models.StringField(default="", low_cardinality=True)
    timestamp = ch_models.DateTime64Field(default=timezone.now)
    created_at = ch_models.DateTime64Field(auto_now_add=True)
    payload = ch_models.StringField(default="empty")

    class Meta:
        ordering = ["-timestamp"]
        engine = ch_models.MergeTree(
            primary_key="event",
            order_by=("event", "timestamp"),
        )

    def __str__(self):
        return self.event
