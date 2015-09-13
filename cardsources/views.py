from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from models import Booster, Deck

def view_booster(request, booster_id):
    booster = get_object_or_404(Booster, pk=booster_id)
    return render(request, 'booster.html', { 'booster': booster })

def view_deck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    return render(request, 'deck.html', { 'deck': deck })

def boosters_list(request):
    boosters = Booster.objects.all
    return render(request, 'boosters_list.html', { 'boosters': boosters })

def decks_list(request):
    decks = Deck.objects.all
    return render(request, 'decks_list.html', { 'decks': decks })
