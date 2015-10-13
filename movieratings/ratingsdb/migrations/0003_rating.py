# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratingsdb', '0002_rater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='ratingsdb.Movie')),
                ('rater', models.ForeignKey(to='ratingsdb.Rater')),
            ],
        ),
    ]
