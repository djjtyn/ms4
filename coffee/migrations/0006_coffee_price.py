# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-26 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_auto_20200325_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.6, max_digits=6),
        ),
    ]
