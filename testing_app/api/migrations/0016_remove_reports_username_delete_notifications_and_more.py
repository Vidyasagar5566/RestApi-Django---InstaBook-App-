# Generated by Django 4.1.6 on 2023-10-15 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0015_remove_allfests_head_remove_allsports_head_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reports",
            name="username",
        ),
        migrations.DeleteModel(
            name="Notifications",
        ),
        migrations.DeleteModel(
            name="Reports",
        ),
    ]