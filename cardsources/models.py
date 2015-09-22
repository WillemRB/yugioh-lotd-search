from django.db import models
from django.template.defaultfilters import slugify

class Player(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    player = models.ForeignKey(Player, related_name='player', null=True)
    opponent = models.ForeignKey(Player, related_name='opponent')

    reverse = models.BooleanField(default=False, help_text='If this is a reverse challenge (from the campaign).')
    challenge_deck = models.BooleanField('Challenge deck', default=False)
    signature_card = models.ForeignKey('cards.Card')

    dlc_name = models.CharField('DLC name', max_length=50, blank=True, help_text='Only fill in this field if the deck requires DLC.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = { 'deck_id': self.pk, 'slug': self.slug }
        return reverse('cardsources.views.view_deck', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Deck, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

class Booster(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    cost = models.IntegerField(default=400)
    serie = models.CharField(
        max_length=10,
        choices = (
            ('original', 'Yu-Gi-Oh'),
            ('gx', 'Yu-Gi-Oh GX'),
            ('5ds', 'Yu-Gi-Oh 5D\'s'),
            ('zexal', 'Yu-Gi-Oh Zexal'),
            ('arc-v', 'Yu-Gi-Oh ARC-V'),
        )
    )
    description = models.TextField(blank=True)
    image_url = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = { 'booster_id': self.id, 'slug': self.slug }
        return reverse('cardsources.views.view_booster', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Booster, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

class BattlePack(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    is_sealed = models.BooleanField('Sealed', default=False)
    is_draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(BattlePack, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
