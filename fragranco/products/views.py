from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all()[:10]
    context = {
        'products': products,
    }
    template = 'products/products_list.html'
    return render(request, template, context)


def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        'product': product,
    }
    template = 'products/product_detail.html'
    return render(request, template, context)
