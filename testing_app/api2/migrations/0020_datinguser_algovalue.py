# Generated by Django 4.1.6 on 2023-11-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0019_rename_reactions_datinguser_reactions1_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="datinguser",
            name="algoValue",
            field=models.FloatField(default=1.0),
        ),
    ]
