# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0007_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
    ]
