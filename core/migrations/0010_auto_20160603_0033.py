# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20160602_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='photos',
            field=models.ManyToManyField(blank=True, null=True, related_name='formations', to='core.Photo'),
        ),
    ]
