from django.db import models
from django.core.urlresolvers import reverse

from cardsources.models import Deck,Booster

class CardType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(help_text='The card text (can include flavour text)', blank=True)

    card_types = models.ManyToManyField(CardType)
    limitation = models.IntegerField(
        choices = (
            (0, 'Forbidden'),
            (1, 'Limited'),
            (2, 'Semi-Limited'),
            (3, 'Unlimited')
        ),
        default=3)
    
    database_id = models.IntegerField(null=True, blank=True, help_text='The Yugioh-Card database id')
    # Changes per printing
    #print_tag = models.CharField(max_length=15, null=True)

    image_url = models.URLField(max_length=200)

    decks = models.ManyToManyField(Deck, blank=True)
    boosters = models.ManyToManyField(Booster, blank=True)

    # Monster card specific
    attribute = models.CharField(
        max_length = 2,
        blank=True,
        choices = (
            (None, 'None'),
            ('dk', 'DARK'),
            ('dv', 'DIVINE'),
            ('ea', 'EARTH'),
            ('fr', 'FIRE'),
            ('lt', 'LIGHT'),
            ('wt', 'WATER'),
            ('wn', 'WIND'),
        ),
    )
    level = models.IntegerField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)

    # Spell card specific
    effect_type = models.CharField(
        max_length = 4,
        blank=True,
        choices = (
            (None, 'None'),
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

    def __str__(self):
        return self.name

    def is_monster(self):
        return self.attribute != None
        
    def is_spell(self):
        return self.effect_type != None

    def get_absolute_url(self):
        return reverse('cards.views.single_card', args=[str(self.id)])

    class Meta:
        ordering = ['name']
