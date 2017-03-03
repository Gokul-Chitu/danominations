# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-02 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0010_auto_20170302_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomination',
            name='reference3',
        ),
        migrations.AlterField(
            model_name='nomination',
            name='faced_disciplinary_action',
            field=models.BooleanField(choices=[(0, 'YES'), (1, 'NO')], default=1),
        ),
    ]
