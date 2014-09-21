# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade_coletada', models.IntegerField()),
                ('enviado_cartorio', models.BooleanField(default=False)),
                ('quantidade_validada', models.IntegerField()),
                ('local_atual', models.ForeignKey(related_name=b'local_atual', to='contador.Cidade')),
                ('local_coleta', models.ForeignKey(related_name=b'local_coleta', to='contador.Cidade')),
                ('responsavel_atual', models.ForeignKey(related_name=b'responsavel_atual', to=settings.AUTH_USER_MODEL)),
                ('responsavel_coleta', models.ForeignKey(related_name=b'responsavel_coleta', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Secao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zona', models.CharField(max_length=3)),
                ('secoes', models.ManyToManyField(to='contador.Secao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coleta',
            name='zona',
            field=models.ForeignKey(to='contador.Zona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(to='contador.Estado'),
            preserve_default=True,
        ),
    ]
