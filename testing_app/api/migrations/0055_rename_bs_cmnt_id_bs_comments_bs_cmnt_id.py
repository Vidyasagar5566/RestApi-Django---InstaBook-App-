# Generated by Django 4.1.6 on 2023-12-01 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0054_buy_sell_bs_comments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bs_comments",
            old_name="BS_cmnt_id",
            new_name="bs_cmnt_id",
        ),
    ]
