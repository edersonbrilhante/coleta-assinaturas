# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zona',
            name='local_zona',
            field=models.ForeignKey(related_name=b'local_zona', default=1, to='contador.Cidade'),
            preserve_default=False,
        ),
    ]
