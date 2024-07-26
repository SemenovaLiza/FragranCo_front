from django.shortcuts import render
from .models import Products, User


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


def get_me(request):
    user = request.user
    bought_products = user.bought_products.all()
    context = {
        'user': user,
        'bought_products': bought_products,
    }
    template = 'users/profile.html'
    return render(request, template, context)


def get_profile_id(request, user_id):
    user = User.objects.get(id=user_id)
    bought_products = user.bought_products.all()
    context = {
        'user': user,
        'bought_products': bought_products,
    }
    template = 'users/profile.html'
    return render(request, template, context)
