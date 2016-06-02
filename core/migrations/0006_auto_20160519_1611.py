# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_photo_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Название видео')),
                ('short_text', models.CharField(blank=True, max_length=300, verbose_name='Краткое описание')),
                ('text', models.TextField(blank=True, verbose_name='Полное описание')),
            ],
        ),
        migrations.CreateModel(
            name='FormationTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Mon', 'Понедельник'), ('Tue', 'Вторник'), ('Wed', 'Среда'), ('Thu', 'Четверг'), ('Fri', 'Пятница'), ('Sat', 'Суббота'), ('Sun', 'Воскресенье')], max_length=3)),
                ('time', models.TimeField()),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formation_times', to='core.Formation')),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.PhotoAlbum'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название Альбома'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='video',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='core.VideoAlbum'),
        ),
        migrations.AddField(
            model_name='formation',
            name='photos',
            field=models.ManyToManyField(related_name='formations', to='core.Photo'),
        ),
    ]