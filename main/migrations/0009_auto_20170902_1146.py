# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170902_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='show_pic',
            field=models.ImageField(upload_to='SMALL'),
        ),
    ]
