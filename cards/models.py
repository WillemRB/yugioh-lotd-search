from django.db import models

# help_text
# null
# choices = ...

class CardType(models.Model):
    name = models.CharField(max_length=20)

class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(help_text='The card text (can include flavour text)')

    card_types = models.ManyToManyField(CardType)
    database_id = models.IntegerField(unique=True, help_text='The Yugioh-Card database id')

    image_url = models.URLField(max_length=200)

    class Meta:
        abstract = True

class MonsterCard(Card):
    attribute = models.CharField(
        max_length = 2,
        choices = (
            ('dk', 'DARK'),
            ('di', 'DIVINE'),
            ('ea', 'EARTH'),
            ('fr', 'FIRE'),
            ('lt', 'LIGHT'),
            ('wa', 'WATER'),
            ('wi', 'WIND'),
        ),
    )
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()

class SpellCard(Card):
    effect_type = models.CharField(
        max_length = 4,
        choices = (
            ('cont', 'Continuous'),
            ('fld', 'Field'),
            ('eq', 'Equip'),
            ('qp', 'Quick-Play'),
            ('rit', 'Ritual'),
            ('coun', 'Counter'),
        )
    )
