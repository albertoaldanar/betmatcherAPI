# Generated by Django 2.0.9 on 2019-10-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
