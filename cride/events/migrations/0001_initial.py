# Generated by Django 2.0.9 on 2019-07-07 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date tieme when the instance was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Date time when object was modified', verbose_name='modified_at')),
                ('top_event', models.BooleanField(default=False)),
                ('in_play', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('score_local', models.PositiveIntegerField(default=0)),
                ('score_visit', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(help_text='Date of the event', verbose_name='event_date')),
                ('traded', models.PositiveIntegerField(default=0)),
                ('top_bet', models.PositiveIntegerField(default=0)),
                ('matched_bets', models.PositiveIntegerField(default=0)),
                ('unmatched_bets', models.PositiveIntegerField(default=0)),
                ('position_local', models.PositiveSmallIntegerField(default=0)),
                ('position_visit', models.PositiveSmallIntegerField(default=0)),
                ('position_draw', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('relation_l_v', models.SmallIntegerField(null=True)),
                ('relation_l_d', models.SmallIntegerField(blank=True, null=True)),
                ('relation_v_d', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date tieme when the instance was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Date time when object was modified', verbose_name='modified_at')),
                ('name', models.CharField(max_length=15)),
                ('show', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(null=True)),
                ('image', models.ImageField(upload_to='', verbose_name='league_image')),
                ('img', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date tieme when the instance was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Date time when object was modified', verbose_name='modified_at')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('icon', models.ImageField(upload_to='users/pictures', verbose_name='sport_icon')),
                ('show', models.BooleanField(default=True)),
                ('img', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date tieme when the instance was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Date time when object was modified', verbose_name='modified_at')),
                ('name', models.CharField(max_length=18, unique=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.League')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='league',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Sport'),
        ),
        migrations.AddField(
            model_name='event',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.League'),
        ),
        migrations.AddField(
            model_name='event',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_team', to='events.Team'),
        ),
        migrations.AddField(
            model_name='event',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Sport'),
        ),
        migrations.AddField(
            model_name='event',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_team', to='events.Team'),
        ),
    ]
