# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150923_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSynthesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u043c\u0430\u043a\u0441. 1000 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)', blank=True)),
                ('tags', models.CharField(max_length=500, verbose_name='\u0422\u0435\u0433\u0438', blank=True)),
                ('literature', models.ManyToManyField(to='core.Literature', verbose_name=b'\xd0\x9b\xd0\xb8\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0441\u0438\u043d\u0442\u0435\u0437\u043e\u0432',
            },
        ),
        migrations.AlterField(
            model_name='synthesis',
            name='literature',
            field=models.ManyToManyField(to='core.Literature', verbose_name=b'\xd0\x9b\xd0\xb8\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0', blank=True),
        ),
    ]
