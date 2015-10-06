# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20151006_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('stars', models.SmallIntegerField()),
                ('movie', models.ForeignKey(to='ratings.Movie')),
                ('rater', models.ForeignKey(to='ratings.Rater')),
            ],
        ),
    ]
