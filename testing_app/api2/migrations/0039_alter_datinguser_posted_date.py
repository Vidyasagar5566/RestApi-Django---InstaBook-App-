# Generated by Django 4.1.6 on 2024-02-11 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0038_alter_datinguser_posted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datinguser',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 11, 18, 49, 50, 593838)),
        ),
    ]
