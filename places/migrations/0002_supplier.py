# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.Place')),
                ('customers', models.ManyToManyField(related_name='provider', to='places.Place')),
            ],
            bases=('places.place',),
        ),
    ]
