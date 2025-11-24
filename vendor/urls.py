from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.vendor_dashboard_view,name='vendor_dashboard'),
    path('upload-item/',views.upload_item_view,name='upload_item'),
    path('orders/',views.vendor_orders_view,name='vendor_orders')
]