# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MonsterCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text=b'The card text (can include flavour text)')),
                ('database_id', models.IntegerField(help_text=b'The Yugioh-Card database id', unique=True)),
                ('image_url', models.URLField()),
                ('attribute', models.CharField(max_length=2, choices=[(b'dk', b'DARK'), (b'di', b'DIVINE'), (b'ea', b'EARTH'), (b'fr', b'FIRE'), (b'lt', b'LIGHT'), (b'wa', b'WATER'), (b'wi', b'WIND')])),
                ('level', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('card_types', models.ManyToManyField(to='cards.CardType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpellCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text=b'The card text (can include flavour text)')),
                ('database_id', models.IntegerField(help_text=b'The Yugioh-Card database id', unique=True)),
                ('image_url', models.URLField()),
                ('effect_type', models.CharField(max_length=4, choices=[(b'cont', b'Continuous'), (b'f', b'Field'), (b'e', b'Equip'), (b'qp', b'Quick-Play'), (b'r', b'Ritual'), (b'c', b'Counter')])),
                ('card_types', models.ManyToManyField(to='cards.CardType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
