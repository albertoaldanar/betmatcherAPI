# Generated by Django 2.0.9 on 2019-10-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_minute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='minute',
            field=models.SmallIntegerField(default=0),
        ),
    ]
