# Generated by Django 2.2.7 on 2019-12-09 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191208_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 9, 20, 57, 9, 549010), verbose_name='Posted'),
        ),
    ]
