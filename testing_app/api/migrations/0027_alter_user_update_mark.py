# Generated by Django 4.1.6 on 2023-10-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0026_user_update_mark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="update_mark",
            field=models.CharField(default="instabook", max_length=11),
        ),
    ]
