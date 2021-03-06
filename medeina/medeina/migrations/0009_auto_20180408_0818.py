# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-08 08:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_states.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medeina', '0008_issue_solved'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueStateLog',
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
        migrations.RemoveField(
            model_name='issuestatuslog',
            name='on',
        ),
        migrations.RemoveField(
            model_name='issuestatuslog',
            name='user',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='status',
            new_name='state',
        ),
        migrations.DeleteModel(
            name='IssueStatusLog',
        ),
        migrations.AddField(
            model_name='issuestatelog',
            name='on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_history', to='medeina.Issue'),
        ),
        migrations.AddField(
            model_name='issuestatelog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
