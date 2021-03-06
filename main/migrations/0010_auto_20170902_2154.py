# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170902_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picface',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='pic',
        ),
        migrations.AddField(
            model_name='picface',
            name='small_pic',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='picname',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='face',
            name='show_pic',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='picface',
            name='source_pic',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='picface',
            name='uid',
            field=models.CharField(max_length=150),
        ),
    ]
