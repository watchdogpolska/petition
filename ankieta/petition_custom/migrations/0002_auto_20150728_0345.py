# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition_custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='small_title',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
