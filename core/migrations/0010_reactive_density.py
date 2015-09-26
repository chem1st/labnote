# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150924_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactive',
            name='density',
            field=models.FloatField(default=10, verbose_name='\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c, \u0433/\u043c\u043b'),
            preserve_default=False,
        ),
    ]
