# Generated by Django 3.2 on 2021-06-07 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0005_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 7, 19, 30, 59, 510140)),
        ),
    ]
