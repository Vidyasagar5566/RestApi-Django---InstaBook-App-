# Generated by Django 4.1.6 on 2023-12-01 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0026_alter_datinguser_posted_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datinguser",
            name="posted_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 1, 0, 23, 8, 147478)
            ),
        ),
    ]
