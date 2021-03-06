# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('face_info', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PicFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('pic', models.ImageField(upload_to='PIC')),
                ('picname', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('username', models.CharField(max_length=150)),
                ('pic', models.ImageField(upload_to='PIC')),
                ('picname', models.CharField(max_length=150)),
                ('is_detected', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
