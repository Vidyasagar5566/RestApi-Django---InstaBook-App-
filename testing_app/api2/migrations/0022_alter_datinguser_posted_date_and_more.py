# Generated by Django 4.1.6 on 2023-11-30 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0021_alter_datinguser_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datinguser",
            name="posted_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 30, 14, 46, 31, 856419)
            ),
        ),
        migrations.AlterField(
            model_name="datinguserreactions",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
