# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-02 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0006_auto_20170302_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomination',
            name='rollno',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
