from django.shortcuts import render
from .models import Products
from django.views.generic import FormView
from .forms import *

def index(request):
    product = Products.objects.all()
    return render(request, 'main/index.html', {'product': product})

def orders(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrdersForm()
        
    return render(request, 'main/orders.html', {'form': form})