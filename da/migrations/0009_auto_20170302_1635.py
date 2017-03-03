# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-02 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0008_auto_20170302_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='mobile_No',
            field=models.CharField(help_text='Only 10 digits', max_length=255),
        ),
        migrations.AlterField(
            model_name='nomination',
            name='req_posistion',
            field=models.CharField(choices=[('President', 'President'), ('Tresurer', 'Tresurer'), ('Secretary', 'Secretary'), ('Joint Secretary', 'Join Secretary')], max_length=255),
        ),
    ]
