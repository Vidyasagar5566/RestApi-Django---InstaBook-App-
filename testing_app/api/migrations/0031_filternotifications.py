# Generated by Django 4.1.6 on 2023-10-24 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0030_alter_alert_comments_img_alter_alerts_img_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FilterNotifications",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lst_buy", models.BooleanField(default=True)),
                ("posts", models.BooleanField(default=True)),
                ("posts_admin", models.BooleanField(default=True)),
                ("events", models.BooleanField(default=True)),
                ("threads", models.BooleanField(default=True)),
                ("comments", models.BooleanField(default=True)),
                ("announcements", models.BooleanField(default=True)),
                ("messanger", models.BooleanField(default=True)),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="FilterNotifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]