# Generated by Django 2.0.9 on 2019-05-24 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_auto_20190524_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date tieme when the instance was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Date time when object was modified', verbose_name='modified_at')),
                ('back_team', models.CharField(max_length=20)),
                ('lay_team', models.CharField(max_length=20)),
                ('is_finished', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('back_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lay', to=settings.AUTH_USER_MODEL)),
                ('lay_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date tieme when the instance was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Date time when object was modified', verbose_name='modified_at')),
                ('back_team', models.CharField(max_length=20)),
                ('is_matched', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('is_public', models.BooleanField(default=True)),
                ('back_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='match',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='matches.Request'),
        ),
    ]
