# Generated by Django 4.1.6 on 2023-12-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0057_alter_buy_sell_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phn_num",
            field=models.CharField(default="0000000000", max_length=10),
        ),
    ]
