# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-16 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0010_auto_20200415_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='description',
        ),
        migrations.AddField(
            model_name='coffee',
            name='overview',
            field=models.CharField(default=1, max_length=200),
        ),
    ]