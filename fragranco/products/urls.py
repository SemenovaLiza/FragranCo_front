from django.urls import path
from .views import index, product_detail


app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]
