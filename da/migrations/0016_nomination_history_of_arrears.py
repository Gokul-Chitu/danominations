# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0015_auto_20170303_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomination',
            name='history_of_arrears',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]