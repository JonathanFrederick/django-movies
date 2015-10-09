# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratings', '0007_remove_rater_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'X')], null=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(null=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(null=True, max_length=5),
        ),
    ]
