# Generated by Django 2.2.6 on 2019-11-15 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 9, 23, 7, 165785, tzinfo=utc)),
        ),
    ]
