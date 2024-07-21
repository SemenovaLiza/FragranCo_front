from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all()[:10]
    context = {
        'products': products,
    }
    template = 'products/products_list.html'
    return render(request, template, context)