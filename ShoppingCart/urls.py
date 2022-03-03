from django.urls import path
from .views import *

app_name = 'cart'  

urlpatterns = [
    path('' , shopping_cart_detail, name='shopping_cart_detail' ),
    path('add/<int:product_id>/' , shopping_cart_add, name='shopping_cart_add' ),
    path('remove/<int:product_id>/', shopping_cart_remove, name='shopping_cart_remove' ),
]