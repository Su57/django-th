# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('th_instapush', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instapush',
            name='app_id',
            field=models.CharField(max_length=255),
        ),
    ]
