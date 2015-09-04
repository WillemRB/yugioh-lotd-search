# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BattlePack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('is_sealed', models.BooleanField(default=False, verbose_name=b'Sealed')),
                ('is_draft', models.BooleanField(default=False, verbose_name=b'Draft')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Booster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField(default=400)),
                ('serie', models.CharField(max_length=10, choices=[(b'original', b'Yu-Gi-Oh'), (b'gx', b'Yu-Gi-Oh GX'), (b'5ds', b"Yu-Gi-Oh 5D's"), (b'zexal', b'Yu-Gi-Oh Zexal'), (b'arc-v', b'Yu-Gi-Oh ARC-V')])),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('challenge_deck', models.BooleanField(default=False)),
                ('dlc', models.BooleanField(default=False)),
                ('dlc_name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(to='cardsources.Player'),
            preserve_default=True,
        ),
    ]
