# Generated by Django 4.1.6 on 2023-10-19 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0025_rename_thread_category_alerts_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="update_mark",
            field=models.CharField(default="instabook", max_length=7),
        ),
    ]
