# Generated by Django 4.1.6 on 2023-10-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_rename_calendersub_branchsub_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="unibranches",
            options={"ordering": ["-branch_name"]},
        ),
        migrations.AddField(
            model_name="unibranches",
            name="priority",
            field=models.CharField(default="CS", max_length=100),
        ),
    ]