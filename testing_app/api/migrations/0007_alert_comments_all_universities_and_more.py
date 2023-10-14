# Generated by Django 4.1.6 on 2023-10-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_user_course_user_is_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="alert_comments",
            name="all_universities",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="alerts",
            name="all_universities",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="events",
            name="all_universities",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="posttable",
            name="all_universities",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_mark",
            field=models.CharField(default="St", max_length=100),
        ),
    ]
