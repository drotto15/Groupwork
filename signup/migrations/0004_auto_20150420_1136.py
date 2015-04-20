# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20150416_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadet',
            name='company',
            field=models.CharField(default='A1', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadet',
            name='sport',
            field=models.CharField(default='sport', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadet',
            name='xNumber',
            field=models.CharField(default=b'x12345', max_length=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meal',
            name='date',
            field=models.DateField(default=-2015, verbose_name=b'Meal Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_description',
            field=models.CharField(default='crispitos', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(default='Breakfast', max_length=2, choices=[(b'BF', b'Breakfast'), (b'BN', b'Brunch'), (b'LU', b'Lunch'), (b'DN', b'Dinner')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
