# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('books', '0001_initial'), ('books', '0002_book_is_published'), ('books', '0003_auto_20170418_2144'), ('books', '0004_auto_20170418_2204')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MS', b'Ms.')], max_length=3)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('authors', models.ManyToManyField(to=b'books.Author')),
                ('is_published', models.BooleanField()),
            ],
        ),
    ]