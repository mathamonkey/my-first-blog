# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20171001_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='freq',
            field=models.IntegerField(default=0),
        ),
    ]
