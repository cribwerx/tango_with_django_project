# Generated by Django 2.1.4 on 2019-01-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20190101_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
