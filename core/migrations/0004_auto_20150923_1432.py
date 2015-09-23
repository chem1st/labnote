# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150923_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labequipment',
            options={'verbose_name': '\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u043e\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435', 'verbose_name_plural': '\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u043e\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435'},
        ),
        migrations.AlterModelOptions(
            name='literature',
            options={'verbose_name': '\u041b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430', 'verbose_name_plural': '\u041b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430'},
        ),
        migrations.AddField(
            model_name='literature',
            name='venue',
            field=models.CharField(default=b'JRN', max_length=3, choices=[(b'JRN', b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd1\x8f \xd0\xb2 \xd0\xb6\xd1\x83\xd1\x80\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb5'), (b'BK', b'\xd0\x9a\xd0\xbd\xd0\xb8\xd0\xb3\xd0\xb0'), (b'RW', b'\xd0\x9e\xd1\x87\xd0\xb5\xd1\x80\xd0\xba'), (b'THS', b'\xd0\xa2\xd0\xb5\xd0\xb7\xd0\xb8\xd1\x81\xd1\x8b'), (b'PRT', b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f')]),
        ),
        migrations.AlterField(
            model_name='literature',
            name='publisher',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
