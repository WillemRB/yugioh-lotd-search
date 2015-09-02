from django.db import models
from cardsources.models import Deck,Booster

class CardType(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(help_text='The card text (can include flavour text)')

    card_types = models.ManyToManyField(CardType)
    limitation = models.IntegerField(default=3)
    database_id = models.IntegerField(unique=True, help_text='The Yugioh-Card database id')

    image_url = models.URLField(max_length=200)
    
    decks = models.ManyToManyField(Deck)
    boosters = models.ManyToManyField(Booster)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class MonsterCard(Card):
    attribute = models.CharField(
        max_length = 2,
        choices = (
            ('dk', 'DARK'),
            ('dv', 'DIVINE'),
            ('ea', 'EARTH'),
            ('fr', 'FIRE'),
            ('lt', 'LIGHT'),
            ('wt', 'WATER'),
            ('wn', 'WIND'),
        ),
    )
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()

class SpellCard(Card):
    effect_type = models.CharField(
        max_length = 4,
        choices = (
            ('con', 'Continuous Spell'),
            ('fld', 'Field Spell'),
            ('eq', 'Equip Spell'),
            ('qp', 'Quick-Play Spell'),
            ('rit', 'Ritual Spell'),
            ('coun', 'Counter Spell'),
            ('cnt', 'Counter Trap'),
            ('cont', 'Continuous Trap'),
            ('nt', 'Normal Trap')
        )
    )
    