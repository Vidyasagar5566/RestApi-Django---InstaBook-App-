# Generated by Django 4.1.6 on 2023-12-01 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0049_alter_alert_comments_posted_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="update_mark",
            field=models.CharField(default="instabook3", max_length=100),
        ),
    ]
