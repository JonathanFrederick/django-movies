# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratingsdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=5, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('occupation', models.PositiveSmallIntegerField(null=True)),
                ('gender', models.CharField(max_length=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
