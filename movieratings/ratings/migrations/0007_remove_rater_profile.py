# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0006_rater_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='profile',
        ),
    ]
