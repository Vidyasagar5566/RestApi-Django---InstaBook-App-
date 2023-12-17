# Generated by Django 4.1.6 on 2023-11-30 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0048_alter_posttable_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alert_comments",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="alerts",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="branchsub",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="branchsubfiles",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="branchsubyears",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="calenderevents",
            name="event_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="calenderevents",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="event_likes",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="events",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="lost_found",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="lst_comments",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="messanger",
            name="message_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="post_comments",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="post_likes",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="posttable",
            name="event_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="posttable",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="ratings",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="unibranches",
            name="posted_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]