# Generated by Django 5.1.4 on 2024-12-17 00:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "devEUI",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("latest_status", models.CharField(default="failing", max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Payload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fCnt", models.BigIntegerField(unique=True)),
                ("data", models.TextField()),
                ("status", models.CharField(default="failing", max_length=10)),
                (
                    "devEUI",
                    models.ForeignKey(
                        db_column="devEUI",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="devices.device",
                    ),
                ),
            ],
        ),
    ]
