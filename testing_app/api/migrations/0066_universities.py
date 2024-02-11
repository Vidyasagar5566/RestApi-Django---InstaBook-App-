# Generated by Django 4.1.6 on 2024-02-11 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_alter_branchsubfiles_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unvName', models.CharField(default='', max_length=100)),
                ('unvLocation', models.CharField(default='', max_length=100)),
                ('unvPic', models.FileField(default='static/img.png', upload_to='pg')),
                ('joinedDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]