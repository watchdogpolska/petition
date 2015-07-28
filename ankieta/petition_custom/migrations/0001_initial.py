# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('thank_you', models.TextField(verbose_name='Thank you text')),
                ('public', models.BooleanField(default=False, verbose_name='Public available')),
                ('main', models.BooleanField(default=True)),
                ('text_top', models.TextField()),
                ('text_bottom', models.TextField()),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Petition',
                'verbose_name_plural': 'Petitions',
            },
            bases=(models.Model,),
        ),
    ]
