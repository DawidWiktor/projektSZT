# Generated by Django 2.0.6 on 2018-12-06 15:18

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atricles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('isBest', models.NullBooleanField()),
                ('background', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
