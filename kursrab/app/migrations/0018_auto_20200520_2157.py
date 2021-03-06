# Generated by Django 3.0.6 on 2020-05-20 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200520_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 20, 21, 57, 34, 390031), verbose_name='Posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 5, 20, 21, 57, 34, 390558), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='released',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 21, 57, 34, 391172), verbose_name='Released'),
        ),
    ]
