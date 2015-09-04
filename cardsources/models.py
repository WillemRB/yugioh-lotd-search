from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Player)

    challenge_deck = models.BooleanField(default=False)
    #signature_card = models.ForeignKey(MonsterCard)

    dlc = models.BooleanField(default=False)
    dlc_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Booster(models.Model):
    name = models.CharField(max_length=50)
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
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class BattlePack(models.Model):
    name = models.CharField(max_length=30)
    is_sealed = models.BooleanField('Sealed', default=False)
    is_draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
