# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0003_auto_20160425_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewer_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
