# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djorm_pgfulltext.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person4',
            name='description_search_index',
        ),
        migrations.RemoveField(
            model_name='person5',
            name='description_search_index',
        ),
        migrations.AddField(
            model_name='person4',
            name='data_search_index',
            field=djorm_pgfulltext.fields.VectorField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
        ),
        migrations.AlterField(
            model_name='person2',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
        ),
        migrations.AlterField(
            model_name='person3',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
        ),
        migrations.AlterField(
            model_name='person4',
            name='data',
            field=models.TextField(default=b'{}'),
        ),
        migrations.AlterField(
            model_name='person4',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
        ),
        migrations.AlterField(
            model_name='person5',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
        ),
    ]
