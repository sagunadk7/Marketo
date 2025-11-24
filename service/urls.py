from django.urls import path
from . import views

urlpatterns = [
    path('order_view/',views.order_view,name='order_view'),
    path('add_to_cart_view/',views.add_to_cart_view,name='add_to_cart_view'),
    path('orders/',views.order_page,name='orders'),
    path('carts/',views.cart_page,name='carts'),
    path('subscribe/',views.subscribe_view,name='subscribe'),
]