from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html', {
        'debug_mode': settings.DEBUG
    })