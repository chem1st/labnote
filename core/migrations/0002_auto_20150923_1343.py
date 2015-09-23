# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reactive',
            options={'ordering': ['cas', 'iupac'], 'verbose_name': '\u0420\u0435\u0430\u043a\u0442\u0438\u0432', 'verbose_name_plural': '\u0420\u0435\u0430\u043a\u0442\u0438\u0432\u044b'},
        ),
        migrations.AlterField(
            model_name='reactive',
            name='cas',
            field=models.CharField(max_length=12, verbose_name='\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 CAS', validators=[django.core.validators.RegexValidator(b'^\\d?-\\d\\d-\\d$')]),
        ),
        migrations.AlterField(
            model_name='reactive',
            name='mm',
            field=models.FloatField(verbose_name='\u041c\u043e\u043b\u044f\u0440\u043d\u0430\u044f \u043c\u0430\u0441\u0441\u0430'),
        ),
    ]
