# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180727_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='userattemptedquiz',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userattemptedquiz',
            name='totalCorrect',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userattemptedquiz',
            name='totalQuestions',
            field=models.IntegerField(default=0),
        ),
    ]