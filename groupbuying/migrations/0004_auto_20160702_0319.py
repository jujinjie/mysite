# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupbuying', '0003_productinfo_isout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Context', models.CharField(max_length=500)),
                ('IsNotice', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': '\u7ba1\u7406\u5458', 'verbose_name_plural': '\u7ba1\u7406\u5458'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': '\u8ba2\u5355', 'verbose_name_plural': '\u8ba2\u5355'},
        ),
        migrations.AlterModelOptions(
            name='productinfo',
            options={'verbose_name': '\u4ea7\u54c1', 'verbose_name_plural': '\u4ea7\u54c1'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
    ]
