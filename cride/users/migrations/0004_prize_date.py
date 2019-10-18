# Generated by Django 2.0.9 on 2019-10-17 19:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date of the event', verbose_name='date'),
        ),
    ]