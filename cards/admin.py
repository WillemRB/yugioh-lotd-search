from django.contrib import admin
from cards.models import CardType,MonsterCard,SpellCard

admin.site.register(CardType)
admin.site.register(MonsterCard)
admin.site.register(SpellCard)
