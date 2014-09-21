# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contador', '0004_auto_20140918_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleta',
            name='quantidade_validada',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
