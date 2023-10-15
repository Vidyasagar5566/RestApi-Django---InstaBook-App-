# Generated by Django 4.1.6 on 2023-10-15 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api2", "0003_remove_allfests_sport_ground"),
    ]

    operations = [
        migrations.CreateModel(
            name="SAC_MEMS",
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
                (
                    "logo",
                    models.ImageField(
                        default="static/img.png", upload_to="club_sports"
                    ),
                ),
                ("img_ratio", models.FloatField(default=1.0)),
                ("role", models.CharField(default="", max_length=100)),
                ("description", models.TextField(default="")),
                ("phone_num", models.CharField(default="", max_length=15)),
                ("email", models.CharField(default="", max_length=50)),
                (
                    "head",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="SAC_MEMS_head",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
