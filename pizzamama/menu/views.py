from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    # pizzas = Pizza.objects.all()
    # pizza_names_and_price = [pizza.nom + " : " + str(pizza.prix) + " $" for pizza in pizzas]
    # pizza_names_and_price_str = ", ".join(pizza_names_and_price)
    # return HttpResponse("Pizzas : " + pizza_names_and_price_str)
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {"pizzas": pizzas})
