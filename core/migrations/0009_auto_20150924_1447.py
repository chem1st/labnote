# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150924_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='synthesis',
            name='products',
        ),
        migrations.AddField(
            model_name='synthesis',
            name='reactives',
            field=models.ManyToManyField(to='core.Reactive', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd1\x8b'),
        ),
    ]
