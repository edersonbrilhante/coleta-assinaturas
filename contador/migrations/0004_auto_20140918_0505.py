# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contador', '0003_auto_20140918_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleta',
            name='quantidade_validada',
            field=models.IntegerField(null=True),
        ),
    ]
