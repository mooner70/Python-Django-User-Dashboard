# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-18 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0003_auto_20180417_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Eddie', max_length=255),
            preserve_default=False,
        ),
    ]
