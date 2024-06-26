# Generated by Django 4.1.6 on 2023-10-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_remove_user_clz_clubs_remove_user_clz_fests_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="clz_clubs",
            field=models.JSONField(default={"head": {}, "team_member": {}}),
        ),
        migrations.AddField(
            model_name="user",
            name="clz_fests",
            field=models.JSONField(default={"head": {}, "team_member": {}}),
        ),
        migrations.AddField(
            model_name="user",
            name="clz_sacs",
            field=models.JSONField(default={"head": {}, "team_member": {}}),
        ),
        migrations.AddField(
            model_name="user",
            name="clz_sports",
            field=models.JSONField(default={"head": {}, "team_member": {}}),
        ),
    ]
