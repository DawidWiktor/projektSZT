# Generated by Django 2.1.4 on 2019-01-10 19:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20181230_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogSignIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=500)),
                ('date', models.TimeField(default=datetime.datetime(2019, 1, 10, 19, 26, 35, 845547, tzinfo=utc))),
                ('isSuccess', models.BinaryField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeLogOff', models.IntegerField(default=300)),
            ],
        ),
    ]
