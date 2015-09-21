from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from cards.models import Card

class Command(BaseCommand):
    def handle(self, *args, **options):
        for card in Card.objects.filter(slug=''):
            # card.save will generate a slug
            card.save()
