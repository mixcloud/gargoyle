# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-25 10:30
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gargoyle', '0002_bytes_to_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='value',
            field=jsonfield.fields.JSONField(default='{}'),
        ),
    ]