# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171020_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='facilityGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=10)),
                ('goalType', models.CharField(max_length=100)),
                ('goalDuration', models.CharField(max_length=100)),
                ('goalAmount', models.IntegerField(max_length=4)),
            ],
        ),
    ]
