# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150923_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='synthesis',
            name='group',
            field=models.ForeignKey(default=10, verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb0', blank=True, to='core.GroupSynthesis'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupsynthesis',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u043c\u0430\u043a\u0441. 1000 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)'),
        ),
        migrations.AlterField(
            model_name='groupsynthesis',
            name='literature',
            field=models.ManyToManyField(to='core.Literature', verbose_name=b'\xd0\x9b\xd0\xb8\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='groupsynthesis',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
