# Generated by Django 4.2.13 on 2024-07-09 07:49

import clickhouse_backend.models
from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event", clickhouse_backend.models.StringField(default="", low_cardinality=True)),
                ("timestamp", clickhouse_backend.models.DateTime64Field(default=django.utils.timezone.now)),
                ("created_at", clickhouse_backend.models.DateTime64Field(auto_now_add=True)),
            ],
            options={
                "ordering": ["-timestamp"],
                "engine": clickhouse_backend.models.MergeTree(order_by=("event", "timestamp"), primary_key="event"),
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("_overwrite_base_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
