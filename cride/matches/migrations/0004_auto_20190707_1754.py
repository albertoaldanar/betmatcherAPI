# Generated by Django 2.0.9 on 2019-07-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20190707_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='opponent',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]