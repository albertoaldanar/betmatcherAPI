# Generated by Django 2.0.9 on 2019-07-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20190707_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='opponent',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
    ]