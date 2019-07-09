# Generated by Django 2.0.9 on 2019-07-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_auto_20190707_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='quote',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='fq',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='message',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='sq',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
