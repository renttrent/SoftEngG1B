# Generated by Django 3.2 on 2021-06-10 10:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboards', '0007_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 12, 10, 15, 443327)),
        ),
        migrations.AlterField(
            model_name='routine',
            name='days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], default=('mon', 'Monday'), max_length=27),
        ),
        migrations.AlterField(
            model_name='routine',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
