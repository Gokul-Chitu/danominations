# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0020_auto_20170306_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='cgpa',
            field=models.CharField(max_length=4),
        ),
    ]