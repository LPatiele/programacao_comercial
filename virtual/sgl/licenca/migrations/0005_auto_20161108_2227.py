# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licenca', '0004_auto_20161108_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requerimentolicenca',
            old_name='statusLicenca',
            new_name='status',
        ),
    ]