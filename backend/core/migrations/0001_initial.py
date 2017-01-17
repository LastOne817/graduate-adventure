# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('semester', models.CharField(max_length=2)),
                ('code', models.CharField(max_length=30)),
                ('number', models.SmallIntegerField(null=True)),
                ('title', models.CharField(max_length=40)),
                ('credit', models.SmallIntegerField()),
                ('category', models.CharField(max_length=10)),
                ('language', models.SmallIntegerField()),
                ('area', models.CharField(max_length=30)),
                ('subarea', models.CharField(max_length=30)),
                ('collage', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=20)),
            ],
        ),
    ]