# Generated by Django 4.1.6 on 2023-12-09 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0060_branchsub_placementcompany_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="calenderevents",
            name="course",
        ),
        migrations.AlterField(
            model_name="calenderevents",
            name="branch",
            field=models.CharField(
                default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE@Other", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="calenderevents",
            name="year",
            field=models.CharField(default="11111", max_length=100),
        ),
    ]
