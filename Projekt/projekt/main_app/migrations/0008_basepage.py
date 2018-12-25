# Generated by Django 2.1.4 on 2018-12-25 18:53

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20181225_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headerImage', models.ImageField(upload_to='')),
                ('background_color', colorful.fields.RGBColorField()),
            ],
        ),
    ]