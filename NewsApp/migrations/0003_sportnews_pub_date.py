# Generated by Django 4.0.1 on 2022-01-20 05:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportnews',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 20, 5, 25, 54, 54832, tzinfo=utc)),
        ),
    ]
