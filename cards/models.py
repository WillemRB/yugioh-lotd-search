from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

from cardsources.models import Deck,Booster

class CardType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Card(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField(help_text='The card text (can include flavour text)', blank=True)

    attribute = models.CharField(
        max_length = 6,
        blank=True,
        choices = (
            (None, 'None'),
            ('dark', 'DARK'),
            ('divine', 'DIVINE'),
            ('earth', 'EARTH'),
            ('fire', 'FIRE'),
            ('light', 'LIGHT'),
            ('water', 'WATER'),
            ('wind', 'WIND'),
        ),
    )
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

    image_url = models.URLField(max_length=200, default='http://i.imgur.com/dLf9fps.png')

    decks = models.ManyToManyField(Deck, blank=True)
    boosters = models.ManyToManyField(Booster, blank=True)

    # Monster card specific
    card_types = models.ManyToManyField(CardType, blank=True)
    level = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)

    # Spell card specific
    effect_type = models.CharField(
        max_length = 20,
        blank=True,
        choices = (
            (None, 'None'),
            ('continuous spell', 'Continuous Spell'),
            ('field spell', 'Field Spell'),
            ('equip spell', 'Equip Spell'),
            ('quickplay spell', 'Quick-Play Spell'),
            ('ritual spell', 'Ritual Spell'),
            ('counter spell', 'Counter Spell'),
            ('counter trap', 'Counter Trap'),
            ('continuous  trap', 'Continuous Trap'),
            ('normal trap', 'Normal Trap')
        )
    )

    def __str__(self):
        return self.name

    def is_monster(self):
        return self.attribute != None
        
    def is_spell(self):
        return self.effect_type != None

    def get_absolute_url(self):
        kwargs = { 'card_id': self.pk, 'slug': self.slug }
        return reverse('cards.views.single_card', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Card, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
