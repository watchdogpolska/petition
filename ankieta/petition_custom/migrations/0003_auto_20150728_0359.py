# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition_custom', '0002_auto_20150728_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='text_read',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='petition',
            name='text_bottom',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
