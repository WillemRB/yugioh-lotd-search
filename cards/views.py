from django.http import HttpResponse
from django.shortcuts import render

from models import MonsterCard, SpellCard

def index(request):
    return HttpResponse("Hello World!")
