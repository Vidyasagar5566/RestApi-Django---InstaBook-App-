# Generated by Django 4.1.6 on 2023-10-15 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_allclubs_allfests_allsports_clubs_likes_fests_likes_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="allfests",
            name="head",
        ),
        migrations.RemoveField(
            model_name="allsports",
            name="head",
        ),
        migrations.RemoveField(
            model_name="clubs_likes",
            name="club",
        ),
        migrations.RemoveField(
            model_name="clubs_likes",
            name="username",
        ),
        migrations.RemoveField(
            model_name="fests_likes",
            name="fest",
        ),
        migrations.RemoveField(
            model_name="fests_likes",
            name="username",
        ),
        migrations.RemoveField(
            model_name="sports_likes",
            name="sport",
        ),
        migrations.RemoveField(
            model_name="sports_likes",
            name="username",
        ),
        migrations.RemoveField(
            model_name="alert_comments",
            name="alert_id",
        ),
        migrations.RemoveField(
            model_name="alerts",
            name="alert_id",
        ),
        migrations.RemoveField(
            model_name="events",
            name="event_id",
        ),
        migrations.RemoveField(
            model_name="lost_found",
            name="lst_id",
        ),
        migrations.RemoveField(
            model_name="lst_comments",
            name="lst_id",
        ),
        migrations.RemoveField(
            model_name="posttable",
            name="post_id",
        ),
        migrations.DeleteModel(
            name="AllClubs",
        ),
        migrations.DeleteModel(
            name="AllFests",
        ),
        migrations.DeleteModel(
            name="AllSports",
        ),
        migrations.DeleteModel(
            name="Clubs_likes",
        ),
        migrations.DeleteModel(
            name="Fests_likes",
        ),
        migrations.DeleteModel(
            name="Sports_likes",
        ),
    ]