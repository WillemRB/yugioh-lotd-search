from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import logging

from models import Card

def index(request):
    return render(request, 'search.html')
    
def search(request):
    query = request.GET.get('q', '')
    
    cards = Card.objects.filter(name__icontains=query)
    
    if cards.count() == 1:
        return render(request, 'card.html', { 'card': cards[0] })
    else:
        return render(request, 'search.html', { 'cards': cards })
    
def single_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'card.html', { 'card': card })
