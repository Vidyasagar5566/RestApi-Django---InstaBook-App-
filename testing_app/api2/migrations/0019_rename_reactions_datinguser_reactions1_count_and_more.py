# Generated by Django 4.1.6 on 2023-11-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0018_datinguser_is_reaction"),
    ]

    operations = [
        migrations.RenameField(
            model_name="datinguser",
            old_name="Reactions",
            new_name="Reactions1_count",
        ),
        migrations.RenameField(
            model_name="datinguser",
            old_name="connections",
            new_name="connections_count",
        ),
        migrations.AddField(
            model_name="datinguser",
            name="Reactions2_count",
            field=models.IntegerField(default=0),
        ),
    ]
