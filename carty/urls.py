from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import add_to_cart, Cart, remove_from_cart, remove_single_item_from_cart, add_single_item_to_cart

urlpatterns = [
    path('cart/', Cart.as_view(), name='cart'),
    #path("cart", cart, name="cart"),
    path("add_to_cart/<int:id>/", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:id>/", remove_from_cart, name="remove_from_cart"),
    path( 'remove_single_item_from_cart/<int:id>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path( 'add_single_item_to_cart/<int:id>/',  add_single_item_to_cart, name= 'add_single_item_to_cart'),
]
