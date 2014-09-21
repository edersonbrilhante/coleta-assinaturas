# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contador', '0002_zona_local_zona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zona',
            name='local_zona',
        ),
        migrations.AddField(
            model_name='zona',
            name='cidade',
            field=models.ForeignKey(default=1, to='contador.Cidade'),
            preserve_default=False,
        ),
    ]
