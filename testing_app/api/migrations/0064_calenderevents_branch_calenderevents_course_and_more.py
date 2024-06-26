# Generated by Django 4.1.6 on 2023-12-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0063_remove_calenderevents_branch_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="calenderevents",
            name="branch",
            field=models.CharField(
                default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE@Other", max_length=100
            ),
        ),
        migrations.AddField(
            model_name="calenderevents",
            name="course",
            field=models.CharField(
                default="B.Tech@M.Tech@PG@Phd@MBA@Other@B.Arch", max_length=100
            ),
        ),
        migrations.AddField(
            model_name="calenderevents",
            name="year",
            field=models.CharField(default="11111", max_length=100),
        ),
    ]
