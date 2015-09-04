from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_GET

from models import Booster

def view_booster(request, booster_id):
    booster = get_object_or_404(Booster, pk=booster_id)
    return render(request, 'booster.html', { 'booster': booster })