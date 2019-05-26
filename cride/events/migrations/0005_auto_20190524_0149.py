# Generated by Django 2.0.9 on 2019-05-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190523_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='in_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='score_local',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='score_visit',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='matched_bets',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='top_bet',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='traded',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='unmatched_bets',
            field=models.PositiveIntegerField(null=True),
        ),
    ]