from django.contrib import admin
from cards.models import CardType, Card

class CardAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }
    fieldsets = [
        (None,           { 'fields': ['name', 'description', 'attribute', 'limitation', 'database_id', 'image_url', 'decks', 'boosters'] }),
        ('Monster Card', { 'fields': ['card_types', 'attack', 'defense', 'level', 'rank'] }),
        ('Spell Card',   { 'fields': ['effect_type'] }),
    ]

admin.site.register(CardType)
admin.site.register(Card, CardAdmin)
