# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-02 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0003_auto_20170302_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomination',
            name='strength1',
        ),
        migrations.RemoveField(
            model_name='nomination',
            name='strength2',
        ),
        migrations.AddField(
            model_name='nomination',
            name='strengths',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
