# Generated by Django 4.1.6 on 2023-12-01 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0023_alter_allclubs_date_of_join_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datinguser",
            name="posted_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 1, 0, 12, 56, 621386)
            ),
        ),
    ]
