# Generated by Django 4.1.6 on 2023-10-12 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_alter_unibranches_options_unibranches_priority"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="unibranches",
            options={"ordering": ["-priority"]},
        ),
    ]
