# Generated by Django 2.1.4 on 2018-12-25 16:08

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_navbar_fontcolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backColor', colorful.fields.RGBColorField(default='#f8f9fa')),
                ('fontColor', colorful.fields.RGBColorField(default='#ffffff')),
            ],
        ),
    ]
