# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-08 10:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import now, utc


class Migration(migrations.Migration):

    dependencies = [
        ('medeina', '0009_auto_20180408_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='solved_on',
            field=models.DateTimeField(null=True),
        ),
    ]
