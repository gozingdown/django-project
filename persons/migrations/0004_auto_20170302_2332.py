# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 04:32
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20170301_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('people', django.db.models.manager.Manager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
    ]