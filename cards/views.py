from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from models import Card

def index(request):
    return render(request, 'card.html')
    
def search(request):
    return render(request, 'search.html')
    
def single_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'card.html', { 'card': card })
