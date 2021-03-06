# Generated by Django 3.0.6 on 2020-05-13 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200513_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 13, 21, 23, 47, 184978), verbose_name='Posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 13, 21, 23, 47, 185399), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='released',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 21, 23, 47, 185919), verbose_name='Released'),
        ),
    ]
