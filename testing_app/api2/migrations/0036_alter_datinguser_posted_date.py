# Generated by Django 4.1.6 on 2023-12-09 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0035_alter_datinguser_posted_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datinguser",
            name="posted_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 21, 3, 6, 580313)
            ),
        ),
    ]
