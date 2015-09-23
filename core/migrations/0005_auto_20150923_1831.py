# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150923_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubform', models.CharField(max_length=3, verbose_name='\u0424\u043e\u0440\u043c\u0430\u0442 \u0438\u0437\u0434\u0430\u043d\u0438\u044f', choices=[(b'JRN', b'\xd0\x96\xd1\x83\xd1\x80\xd0\xbd\xd0\xb0\xd0\xbb'), (b'BK', b'\xd0\x9a\xd0\xbd\xd0\xb8\xd0\xb3\xd0\xb0'), (b'RW', b'\xd0\x9e\xd1\x87\xd0\xb5\xd1\x80\xd0\xba'), (b'THS', b'\xd0\xa2\xd0\xb5\xd0\xb7\xd0\xb8\xd1\x81\xd1\x8b'), (b'PRT', b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f')])),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('publisher', models.CharField(max_length=100, verbose_name='\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='literature',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='literature',
            name='venue',
        ),
        migrations.AddField(
            model_name='literature',
            name='url',
            field=models.URLField(default=b'http://www.acs.org'),
        ),
        migrations.AlterField(
            model_name='literature',
            name='author',
            field=models.CharField(max_length=100, verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='literature',
            name='title',
            field=models.CharField(max_length=300, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='literature',
            name='edition',
            field=models.ForeignKey(default=b'1', to='core.Edition'),
        ),
    ]
