# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20151007_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'X')], default='X', max_length=1),
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.CharField(default='00', max_length=40),
        ),
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]
