from django.shortcuts import render,redirect
from datetime import datetime
from vendor.models import ItemsDescription,Orders
def store(request):
    food = ItemsDescription.objects.all()
    print(food)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity',1))
        item = request.POST.get('item')
        print(f"Someone has ordered {quantity} {item} at {datetime.now().replace(microsecond=0)}.")
    return render(request,'index.html',{'foods':food})

def order_view(request):
    print('Order Recieved')
    if request.method == 'POST':
            quantities = request.POST.get('quantity',1)
            item = request.POST.get('item')
            order_by_name = request.POST.get('username')
            order=Orders(quantity=quantities,order_by=order_by_name,item_name=item)
            order.save()
            print("Ordered Saved")
            return redirect('index')


def add_to_cart_view(request):
    return redirect('index')

def order_page(request):
    return render(request,'order.html')

def cart_page(request):
    return render(request,'cart.html')
# Create your views here.
