# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardsources', '0001_initial'),
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
                ('limitation', models.IntegerField(default=3)),
                ('database_id', models.IntegerField(help_text=b'The Yugioh-Card database id', unique=True)),
                ('image_url', models.URLField()),
                ('attribute', models.CharField(max_length=2, choices=[(b'dk', b'DARK'), (b'dv', b'DIVINE'), (b'ea', b'EARTH'), (b'fr', b'FIRE'), (b'lt', b'LIGHT'), (b'wt', b'WATER'), (b'wn', b'WIND')])),
                ('level', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('boosters', models.ManyToManyField(to='cardsources.Booster')),
                ('card_types', models.ManyToManyField(to='cards.CardType')),
                ('decks', models.ManyToManyField(to='cardsources.Deck')),
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
                ('limitation', models.IntegerField(default=3)),
                ('database_id', models.IntegerField(help_text=b'The Yugioh-Card database id', unique=True)),
                ('image_url', models.URLField()),
                ('effect_type', models.CharField(max_length=4, choices=[(b'con', b'Continuous Spell'), (b'fld', b'Field Spell'), (b'eq', b'Equip Spell'), (b'qp', b'Quick-Play Spell'), (b'rit', b'Ritual Spell'), (b'coun', b'Counter Spell'), (b'cnt', b'Counter Trap'), (b'cont', b'Continuous Trap'), (b'nt', b'Normal Trap')])),
                ('boosters', models.ManyToManyField(to='cardsources.Booster')),
                ('card_types', models.ManyToManyField(to='cards.CardType')),
                ('decks', models.ManyToManyField(to='cardsources.Deck')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
