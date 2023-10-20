# Generated by Django 4.1.6 on 2023-10-15 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api2", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reports",
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
                ("description", models.TextField(default="")),
                ("report_belongs", models.CharField(default="student", max_length=100)),
                (
                    "posted_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("domain", models.TextField(default="@nitc.ac.in")),
                (
                    "username",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ReportUser",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notifications",
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
                ("title", models.CharField(default="", max_length=100)),
                ("description", models.TextField(default="")),
                ("branch", models.CharField(default="@", max_length=100)),
                (
                    "batch",
                    models.CharField(
                        default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE", max_length=100
                    ),
                ),
                ("year", models.CharField(default="1111", max_length=100)),
                ("img", models.FileField(default="static/img.png", upload_to="notif")),
                ("img_ratio", models.FloatField(default=1.0)),
                (
                    "posted_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("domain", models.TextField(default="@nitc.ac.in")),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Notification_username",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-posted_date"],
            },
        ),
    ]