# Generated by Django 3.2.4 on 2021-06-13 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_auto_20210613_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminnotes',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 14, 43, 8, 256792)),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='ends_work_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 14, 43, 8, 256792)),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='starts_work_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 14, 43, 8, 256792)),
        ),
    ]
