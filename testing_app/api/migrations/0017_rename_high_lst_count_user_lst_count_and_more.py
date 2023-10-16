# Generated by Django 4.1.6 on 2023-10-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_remove_reports_username_delete_notifications_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="high_lst_count",
            new_name="lst_count",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="high_post_count",
            new_name="post_count",
        ),
        migrations.AddField(
            model_name="user",
            name="clubs",
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name="user",
            name="clz_clubs_head",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="clz_fests_head",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="clz_sac_head",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="clz_sports_head",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="fests",
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name="user",
            name="sac",
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name="user",
            name="sports",
            field=models.JSONField(default={}),
        ),
    ]
