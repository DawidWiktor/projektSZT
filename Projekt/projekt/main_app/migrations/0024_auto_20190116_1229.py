# Generated by Django 2.1.4 on 2019-01-16 11:29

import colorful.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_auto_20190114_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'AboutMe', 'verbose_name_plural': 'AboutMe'},
        ),
        migrations.AlterModelOptions(
            name='atricles',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='basepage',
            options={'verbose_name': 'BasePage', 'verbose_name_plural': 'BasePage'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Footer', 'verbose_name_plural': 'Footer'},
        ),
        migrations.AlterModelOptions(
            name='logsignin',
            options={'verbose_name': 'LogSignin', 'verbose_name_plural': 'LogSignin'},
        ),
        migrations.AlterModelOptions(
            name='messages',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='navbar',
            options={'verbose_name': 'Navbar', 'verbose_name_plural': 'Navbar'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
        migrations.AddField(
            model_name='basepage',
            name='colorButton',
            field=colorful.fields.RGBColorField(default='#17a2b8'),
        ),
        migrations.AlterField(
            model_name='logsignin',
            name='date',
            field=models.TimeField(default=datetime.datetime(2019, 1, 16, 11, 29, 21, 359272, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.TimeField(default=datetime.datetime(2019, 1, 16, 11, 29, 21, 359272, tzinfo=utc)),
        ),
    ]