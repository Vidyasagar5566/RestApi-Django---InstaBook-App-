# Generated by Django 4.1.6 on 2023-10-13 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_branchsub_course_branchsubfiles_course_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reports",
            name="username",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ReportUser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]