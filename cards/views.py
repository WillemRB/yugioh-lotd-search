from django.http import HttpResponse
from django.shortcuts import render

from models import Card

def index(request):
    return HttpResponse("Hello World!")
