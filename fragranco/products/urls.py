from django.urls import path
from .views import index, product_detail, get_me, get_profile_id


app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('users/me/', get_me, name='profile'),
    path('users/<int:user_id>/', get_profile_id, name='profile_id')
]
