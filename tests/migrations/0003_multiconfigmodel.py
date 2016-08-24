# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djorm_pgfulltext.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20160823_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiConfigModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('search_index', djorm_pgfulltext.fields.VectorField()),
            ],
        ),
    ]
