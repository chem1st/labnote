# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150923_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'ordering': ['sample_id'], 'verbose_name': '\u0410\u043d\u0430\u043b\u0438\u0437', 'verbose_name_plural': '\u041c\u0435\u0442\u043e\u0434\u044b \u0430\u043d\u0430\u043b\u0438\u0437\u0430'},
        ),
        migrations.AlterModelOptions(
            name='edition',
            options={'ordering': ['title'], 'verbose_name': '\u0418\u0437\u0434\u0430\u043d\u0438\u0435', 'verbose_name_plural': '\u0418\u0437\u0434\u0430\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='literature',
            options={'ordering': ['title'], 'verbose_name': '\u041b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430', 'verbose_name_plural': '\u041b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430'},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name': '\u0421\u0442\u0430\u0434\u0438\u044f', 'verbose_name_plural': '\u0421\u0442\u0430\u0434\u0438\u0438 \u0441\u0438\u043d\u0442\u0435\u0437\u0430'},
        ),
        migrations.AlterModelOptions(
            name='synthesis',
            options={'ordering': ['-date'], 'verbose_name': '\u0421\u0438\u043d\u0442\u0435\u0437', 'verbose_name_plural': '\u0421\u0438\u043d\u0442\u0435\u0437\u044b'},
        ),
        migrations.AlterField(
            model_name='analysis',
            name='data',
            field=models.FileField(upload_to=b'', verbose_name='\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435'),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='img',
            field=models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='method',
            field=models.CharField(max_length=5, verbose_name='\u041c\u0435\u0442\u043e\u0434 \u0430\u043d\u0430\u043b\u0438\u0437\u0430', choices=[(b'NMR', b'\xd0\xaf\xd0\x9c\xd0\xa0'), (b'IR', b'\xd0\x98\xd0\x9a'), (b'GPC', b'\xd0\x93\xd0\x9f\xd0\xa5'), (b'ELEM', b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9'), (b'MASS', b'\xd0\x9c\xd0\xb0\xd1\x81\xd1\x81-\xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x8f'), (b'MALDI', b'MALDI-TOF \xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x8f'), (b'CMASS', b'\xd0\xa5\xd1\x80\xd0\xbe\xd0\xbc\xd0\xb0\xd1\x82\xd0\xbe-\xd0\xbc\xd0\xb0\xd1\x81\xd1\x81 \xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x8f')]),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='sample_id',
            field=models.CharField(max_length=10, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043e\u0431\u0440\u0430\u0437\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='spectrum_id',
            field=models.CharField(max_length=10, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u043f\u0435\u043a\u0442\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='literature',
            name='edition',
            field=models.ForeignKey(verbose_name=b'\xd0\x98\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', to='core.Edition'),
        ),
        migrations.AlterField(
            model_name='literature',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='reactive',
            name='bp',
            field=models.SmallIntegerField(null=True, verbose_name='\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043a\u0438\u043f\u0435\u043d\u0438\u044f, \u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='reactive',
            name='mm',
            field=models.FloatField(verbose_name='\u041c\u043e\u043b\u044f\u0440\u043d\u0430\u044f \u043c\u0430\u0441\u0441\u0430, \u0433/\u043c\u043e\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='reactive',
            name='mp',
            field=models.SmallIntegerField(null=True, verbose_name='\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043f\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u044f, \u0421', blank=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u0442\u0430\u0434\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='description',
            field=models.TextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='end',
            field=models.TimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='is_complex',
            field=models.BooleanField(default=False, verbose_name='\u0423 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 \u0441\u043b\u043e\u0436\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u044b \u0438/\u0438\u043b\u0438 \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='name',
            field=models.CharField(max_length=300, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='p',
            field=models.IntegerField(default=765, verbose_name='\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435, \u043c\u043c.\u0440\u0442.\u0441\u0442.'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='reactives',
            field=models.ManyToManyField(related_name='reactives', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd1\x8b', to='core.Reactive'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='solvents',
            field=models.ManyToManyField(related_name='solvents', verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe\xd1\x80\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to='core.Reactive', blank=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='start',
            field=models.TimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='synthesis',
            field=models.ForeignKey(related_name='stages', to='core.Synthesis'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='t',
            field=models.IntegerField(default=20, verbose_name='\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430, C'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='yield_percent',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0412\u044b\u0445\u043e\u0434 \u043d\u0430 \u0441\u0442\u0430\u0434\u0438\u0438, %', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='synthesis',
            name='date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0438\u043d\u0442\u0435\u0437\u0430'),
        ),
        migrations.AlterField(
            model_name='synthesis',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u043c\u0430\u043a\u0441. 1000 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)', blank=True),
        ),
        migrations.AlterField(
            model_name='synthesis',
            name='literature',
            field=models.ManyToManyField(to='core.Literature', verbose_name=b'\xd0\x9b\xd0\xb8\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='synthesis',
            name='products',
            field=models.ManyToManyField(to='core.Reactive', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb4\xd1\x83\xd0\xba\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='synthesis',
            name='tags',
            field=models.CharField(max_length=500, verbose_name='\u0422\u0435\u0433\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='synthesis',
            name='yield_percent',
            field=models.IntegerField(verbose_name=b'\xd0\x92\xd1\x8b\xd1\x85\xd0\xbe\xd0\xb4 \xd1\x86\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb4\xd1\x83\xd0\xba\xd1\x82\xd0\xb0, %', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
