# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='comment',
        ),
        migrations.AddField(
            model_name='class',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='basics.Answer'),
        ),
        migrations.AddField(
            model_name='comment',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='basics.Answer'),
        ),
    ]
