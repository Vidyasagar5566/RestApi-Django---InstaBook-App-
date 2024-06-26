# Generated by Django 4.1.6 on 2023-10-11 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_remove_alert_comments_all_universities"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CalenderSub",
            new_name="BranchSub",
        ),
        migrations.RenameModel(
            old_name="CalenderSubFiles",
            new_name="BranchSubFiles",
        ),
        migrations.RenameModel(
            old_name="CalenderSubYears",
            new_name="BranchSubYears",
        ),
        migrations.CreateModel(
            name="UniBranches",
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
                    "course",
                    models.CharField(
                        choices=[
                            ("B.Tech", "B.Tech"),
                            ("M.Tech", "M.Tech"),
                            ("PG", "PG"),
                            ("Phd", "Phd"),
                            ("MBA", "MBA"),
                        ],
                        default="CS",
                        max_length=100,
                    ),
                ),
                ("branch_name", models.CharField(default="CS", max_length=100)),
                ("semisters", models.TextField(default="")),
                (
                    "posted_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("domain", models.TextField(default="@nitc.ac.in")),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="UniBranches_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
