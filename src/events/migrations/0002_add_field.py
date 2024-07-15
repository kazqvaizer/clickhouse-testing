# Generated by Django 4.2.13 on 2024-07-09 08:17

import clickhouse_backend.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_init_clickhouse_events"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="payload",
            field=clickhouse_backend.models.StringField(default="empty"),
        ),
    ]