# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cadet',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='signup.User')),
            ],
            options={
            },
            bases=('signup.user',),
        ),
        migrations.RemoveField(
            model_name='meal',
            name='meal_date',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='meal_description',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='meal_type',
        ),
    ]
