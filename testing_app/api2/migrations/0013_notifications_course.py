# Generated by Django 4.1.6 on 2023-11-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0012_alter_datinguser_options_datinguser_posted_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="notifications",
            name="course",
            field=models.CharField(
                default="B.Tech@M.Tech@PG@Phd@MBA@Other", max_length=100
            ),
        ),
    ]
