# Generated by Django 4.1.6 on 2023-10-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0004_sac_mems"),
    ]

    operations = [
        migrations.AddField(
            model_name="sac_mems",
            name="domain",
            field=models.TextField(default="@nitc.ac.in"),
        ),
    ]