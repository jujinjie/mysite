# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 08:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupbuying', '0007_auto_20160702_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinfo',
            name='ProductImage',
        ),
    ]