# Generated by Django 3.2.4 on 2021-06-13 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_auto_20210613_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminnotes',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 13, 3, 30, 6941)),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='ends_work_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 13, 3, 30, 7944)),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='starts_work_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 13, 3, 30, 7944)),
        ),
    ]
