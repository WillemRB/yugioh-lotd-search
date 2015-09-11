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
    
def single_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'card.html', { 'card': card })
    
def report_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'report.html', { 'card': card })
    
def report_card_submit(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    
    report_message = request.POST.get('report')
    
    if len(report_message) == 0:
        return render(request, 'report.html', { 'card': card, 'error': 'No description was provided!' })

    headers = { 'Authorization': 'Bearer ' + os.getenv('ASANA_ACCESSKEY') }
    payload = { 'data': 
        { 
            'name': card.name, 
            'notes': report_message, 
            'workspace': long(os.getenv('ASANA_WORKSPACEID')), 
            'projects': [ long(os.getenv('ASANA_PROJECTID')) ] 
        } 
    }
    
    resp = requests.post("https://app.asana.com/api/1.0/tasks", data=json.dumps(payload), headers=headers)
    
    if resp.status_code == 201:
        return render(request, 'report.html', { 'card': card, 'message': 'Thank you for your contribution.' })
    else:
        return render(request, 'report.html', { 'card': card, 'error': 'An error occured while sending the request.' })
    