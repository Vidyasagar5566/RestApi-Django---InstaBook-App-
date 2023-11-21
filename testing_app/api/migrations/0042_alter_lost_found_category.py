# Generated by Django 4.1.6 on 2023-11-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0041_lost_found_category_lost_found_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lost_found",
            name="category",
            field=models.CharField(
                choices=[
                    ("all", "all"),
                    ("cards", "cards"),
                    ("essentials", "essentials"),
                    ("smartDevices", "smartDevices"),
                    ("belongings", "belongings"),
                    ("valuables", "valuables"),
                    ("clothings", "clothings"),
                    ("rideShares", "rideShares"),
                    ("usedCampusItems", "usedCampusItems"),
                    ("houseSharings", "houseSharings"),
                    ("others", "others"),
                ],
                default="belongings",
                max_length=50,
            ),
        ),
    ]
