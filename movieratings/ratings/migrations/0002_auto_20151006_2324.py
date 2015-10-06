# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=215)),
                ('movie', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='rater',
            old_name='rater_id',
            new_name='rater',
        ),
    ]
