# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 15:16
from __future__ import unicode_literals

import asset_manager.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_manager', '0002_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='f1', upload_to=asset_manager.utils.get_file_directory_path),
            preserve_default=False,
        ),
    ]