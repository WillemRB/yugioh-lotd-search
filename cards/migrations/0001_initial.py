# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardsources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text=b'The card text (can include flavour text)', blank=True)),
                ('limitation', models.IntegerField(default=3, choices=[(0, b'Forbidden'), (1, b'Limited'), (2, b'Semi-Limited'), (3, b'None')])),
                ('database_id', models.IntegerField(help_text=b'The Yugioh-Card database id', null=True, blank=True)),
                ('image_url', models.URLField()),
                ('attribute', models.CharField(blank=True, max_length=2, choices=[(None, b'None'), (b'dk', b'DARK'), (b'dv', b'DIVINE'), (b'ea', b'EARTH'), (b'fr', b'FIRE'), (b'lt', b'LIGHT'), (b'wt', b'WATER'), (b'wn', b'WIND')])),
                ('level', models.IntegerField(null=True, blank=True)),
                ('stars', models.IntegerField(null=True, blank=True)),
                ('attack', models.IntegerField(null=True, blank=True)),
                ('defense', models.IntegerField(null=True, blank=True)),
                ('effect_type', models.CharField(blank=True, max_length=4, choices=[(None, b'None'), (b'con', b'Continuous Spell'), (b'fld', b'Field Spell'), (b'eq', b'Equip Spell'), (b'qp', b'Quick-Play Spell'), (b'rit', b'Ritual Spell'), (b'coun', b'Counter Spell'), (b'cnt', b'Counter Trap'), (b'cont', b'Continuous Trap'), (b'nt', b'Normal Trap')])),
                ('boosters', models.ManyToManyField(to='cardsources.Booster', blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='card_types',
            field=models.ManyToManyField(to='cards.CardType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='decks',
            field=models.ManyToManyField(to='cardsources.Deck', blank=True),
            preserve_default=True,
        ),
    ]
