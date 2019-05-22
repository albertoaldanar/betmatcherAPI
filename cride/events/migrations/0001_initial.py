# Generated by Django 2.0.9 on 2019-05-22 22:41

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
                ('local', models.CharField(max_length=15, unique=True)),
                ('visit', models.CharField(max_length=15, unique=True)),
                ('date', models.DateTimeField(help_text='Date of the event', verbose_name='event_date')),
                ('traded', models.PositiveIntegerField(default=0)),
                ('top_bet', models.PositiveIntegerField(default=0)),
                ('matched_bets', models.PositiveIntegerField(default=0)),
                ('unmatched_bets', models.PositiveIntegerField(default=0)),
                ('position_local', models.PositiveSmallIntegerField(default=0)),
                ('position_visit', models.PositiveSmallIntegerField(default=0)),
                ('position_draw', models.PositiveSmallIntegerField(default=0)),
                ('relation_l_v', models.SmallIntegerField(null=True)),
                ('relation_l_d', models.SmallIntegerField(null=True)),
                ('relation_v_d', models.SmallIntegerField(null=True)),
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
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Sport'),
        ),
    ]
