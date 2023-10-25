from django.shortcuts import render
from .models import *

def index(request):
    product = Products.objects.all()
    return render(request, 'main/index.html', {'product': product})
