from django.contrib import admin
from models import Deck, Booster, BattlePack

class DeckAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }

class BoosterAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }

class BattlePackAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }

admin.site.register(Deck)
admin.site.register(Booster)
admin.site.register(BattlePack)
