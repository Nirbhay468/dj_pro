# Generated by Django 4.0.1 on 2022-01-20 17:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0004_news_pub_date_alter_sportnews_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 20, 17, 27, 22, 945596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sportnews',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 20, 17, 27, 23, 37614, tzinfo=utc)),
        ),
    ]