# Generated by Django 4.1.6 on 2023-09-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_user_domain_user_notif_settings"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_sac",
            new_name="is_student_admin",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="sac_role",
            new_name="student_admin_role",
        ),
        migrations.AddField(
            model_name="user",
            name="instabook_role",
            field=models.CharField(default="@", max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="is_instabook",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="skills",
            field=models.JSONField(
                default={
                    "Education_details": {},
                    "Programming_Languages": "",
                    "Projects": {},
                    "Work_Experience": {},
                }
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="star_mark",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="user_mark",
            field=models.CharField(default="Student", max_length=100),
        ),
    ]
