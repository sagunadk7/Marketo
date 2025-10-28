from django.urls import path
from . import views

urlpatterns = [
    path('store/',views.store,name='store'),
    path('order_view/',views.order_view,name='order_view'),
    path('add_to_cart_view/',views.add_to_cart_view,name='add_to_cart_view'),
    path('orders/',views.order_page,name='orders'),
    path('carts/',views.cart_page,name='carts')
]