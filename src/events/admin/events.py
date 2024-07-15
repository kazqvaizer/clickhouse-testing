from django.contrib import admin

from app.admin import ModelAdmin
from events.models import Event


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = [
        "event",
        "timestamp",
        "created_at",
        "payload",
    ]
