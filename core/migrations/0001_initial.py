# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('method', models.CharField(max_length=5, choices=[(b'NMR', b'\xd0\xaf\xd0\x9c\xd0\xa0'), (b'IR', b'\xd0\x98\xd0\x9a'), (b'GPC', b'\xd0\x93\xd0\x9f\xd0\xa5'), (b'ELEM', b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9'), (b'MASS', b'\xd0\x9c\xd0\xb0\xd1\x81\xd1\x81-\xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x8f'), (b'MALDI', b'MALDI-TOF \xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x8f'), (b'CMASS', b'\xd0\xa5\xd1\x80\xd0\xbe\xd0\xbc\xd0\xb0\xd1\x82\xd0\xbe-\xd0\xbc\xd0\xb0\xd1\x81\xd1\x81 \xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x8f')])),
                ('sample_id', models.CharField(max_length=10)),
                ('spectrum_id', models.CharField(max_length=10)),
                ('data', models.FileField(upload_to=b'')),
                ('img', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='LabEquipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipment_type', models.CharField(max_length=5, choices=[(b'GLASS', b'\xd1\x81\xd1\x82\xd0\xb5\xd0\xba\xd0\xbb\xd1\x8f\xd0\xbd\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x81\xd1\x83\xd0\xb4\xd0\xb0'), (b'METAL', b'\xd0\xbc\xd0\xb5\xd1\x82\xd0\xb0\xd0\xbb\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x81\xd1\x83\xd0\xb4\xd0\xb0'), (b'ADD', b'\xd0\xb4\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5')])),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reactive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cas', models.CharField(max_length=12, verbose_name='\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 CAS', validators=[django.core.validators.RegexValidator(b'^\\d\\d-\\d\\d-\\d$')])),
                ('iupac', models.CharField(max_length=300, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0435 \u0418\u042e\u041f\u0410\u041a')),
                ('rational', models.CharField(max_length=300, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e \u0440\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0439 \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0435', blank=True)),
                ('trivial', models.CharField(max_length=300, verbose_name='\u0422\u0440\u0438\u0432\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('formula', models.CharField(max_length=50, verbose_name='\u0411\u0440\u0443\u0442\u0442\u043e \u0444\u043e\u0440\u043c\u0443\u043b\u0430')),
                ('img', models.ImageField(upload_to=b'', verbose_name='\u0413\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
                ('mm', models.PositiveIntegerField(verbose_name='\u041c\u043e\u043b\u044f\u0440\u043d\u0430\u044f \u043c\u0430\u0441\u0441\u0430')),
                ('appearance', models.CharField(max_length=150, verbose_name='\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0432\u0438\u0434', blank=True)),
                ('mp', models.SmallIntegerField(verbose_name='\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043f\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u044f', blank=True)),
                ('bp', models.SmallIntegerField(verbose_name='\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043a\u0438\u043f\u0435\u043d\u0438\u044f', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=1000)),
                ('is_complex', models.BooleanField(default=False)),
                ('t', models.IntegerField(default=20)),
                ('p', models.IntegerField(default=765)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('yield_percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('reactives', models.ManyToManyField(related_name='reactives', to='core.Reactive')),
                ('solvents', models.ManyToManyField(related_name='solvents', to='core.Reactive')),
            ],
        ),
        migrations.CreateModel(
            name='Synthesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=1000, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('tags', models.CharField(max_length=500)),
                ('yield_percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('literature', models.ManyToManyField(to='core.Literature')),
                ('products', models.ManyToManyField(to='core.Reactive')),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='synthesis',
            field=models.ForeignKey(to='core.Synthesis'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='stage',
            field=models.ForeignKey(to='core.Stage'),
        ),
    ]
