# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160602_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.PhotoAlbum'),
        ),
        migrations.AlterField(
            model_name='video',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='core.VideoAlbum'),
        ),
    ]
