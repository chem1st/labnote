# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150923_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactive',
            name='bp',
            field=models.SmallIntegerField(null=True, verbose_name='\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043a\u0438\u043f\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='reactive',
            name='cas',
            field=models.CharField(max_length=12, verbose_name='\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 CAS', validators=[django.core.validators.RegexValidator(b'^\\d+-\\d\\d-\\d$')]),
        ),
        migrations.AlterField(
            model_name='reactive',
            name='mp',
            field=models.SmallIntegerField(null=True, verbose_name='\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043f\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u044f', blank=True),
        ),
    ]
