# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0003_auto_20160228_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='problemType',
            field=models.CharField(default='MULTIPLE_CHOICE', max_length=1000),
        ),
    ]