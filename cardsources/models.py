from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Player)

    challenge_deck = models.BooleanField(default=False)

    dlc = models.BooleanField(default=False)
    dlc_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Booster(models.Model):
    name = models.CharField(max_length=50)
    serie = models.CharField(
        max_length=10,
        choices = (
            ('original', 'Yu-Gi-Oh'),
            ('gx', 'Yu-Gi-Oh GX'),
            ('5ds', 'Tu-Gi-Oh 5Ds'),
        )
    )

    def __str__(self):
        return self.name