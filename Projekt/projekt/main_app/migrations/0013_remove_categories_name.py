# Generated by Django 2.1.4 on 2018-12-25 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_atricles_categoryid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='name',
        ),
    ]