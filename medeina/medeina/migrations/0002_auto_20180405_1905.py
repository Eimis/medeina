# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 19:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_states.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medeina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueStatusLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_states.fields.StateField(default=b'transition_initiated', max_length=100, verbose_name='state id')),
                ('from_state', models.CharField(choices=[(b'solved', b'Issue is solved'), (b'open', b'Issue is open')], max_length=100)),
                ('to_state', models.CharField(choices=[(b'solved', b'Issue is solved'), (b'open', b'Issue is open')], max_length=100)),
                ('serialized_kwargs', models.TextField(blank=True)),
                ('start_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='transition started at')),
            ],
            options={
                'verbose_name': 'issue transition',
            },
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=django_states.fields.StateField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='issuestatuslog',
            name='on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_history', to='medeina.Issue'),
        ),
        migrations.AddField(
            model_name='issuestatuslog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
