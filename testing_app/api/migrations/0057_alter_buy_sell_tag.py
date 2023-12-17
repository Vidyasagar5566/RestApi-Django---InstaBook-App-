# Generated by Django 4.1.6 on 2023-12-01 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0056_alter_bs_comments_bs_cmnt_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buy_sell",
            name="tag",
            field=models.CharField(
                choices=[
                    ("lost", "lost"),
                    ("found", "found"),
                    ("buy", "buy"),
                    ("sell", "sell"),
                ],
                default="buy",
                max_length=50,
            ),
        ),
    ]