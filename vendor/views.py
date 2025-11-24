from django.shortcuts import render
from .decorators import vendor_required
@vendor_required
def vendor_dashboard_view(request):
    return render(request, 'dashboard.html')
@vendor_required
def upload_item_view(request):
    return render(request,'upload_item.html')
@vendor_required
def vendor_orders_view(request):
    return render(request,'vendor_orders.html')

# Create your views here.
