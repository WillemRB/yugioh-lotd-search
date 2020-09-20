import os
import requests
import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from models import Card

def search(request):
    query = request.GET.get('q', None)
    
    if query is None:
        return render(request, 'search.html')

    cards = Card.objects.filter(name__icontains=query)
    
    if cards.count() == 1:
        return redirect(cards[0])
    else:
        return render(request, 'search.html', { 'cards': cards, 'query': query })
    
def single_card(request, card_id, slug):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'card.html', { 'card': card })
    
    