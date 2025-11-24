from django.shortcuts import render,redirect,get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from decimal import Decimal, ROUND_HALF_UP
from django.db import transaction
from datetime import datetime
from vendor.models import Product,Order
from accounts.models import CustomUser
from vendor.decorators import customer_required
from service.models import SubscribedUser
def store(request):
    product = Product.objects.all()
    print(product)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity',1))
        item = request.POST.get('item')
        print(f"Someone has ordered {quantity} {item} at {datetime.now().replace(microsecond=0)}.")
    return render(request,'index.html',{'product':product})

def order_view(request):
    print('Order Recieved')
    if request.method != "POST":
        messages.error(request,"Invalid request method.")
        return redirect('store')
    user = request.user
    if not user.is_authenticated:
        messages.error(request,'You must be logged in to place a order.')
        return redirect('store')
    product_id = request.POST.get('product_id')
    if not product_id:
        messages.error(request,"No product selected.")
        return redirect('store')
    product = Product.objects.filter(pk=product_id).first()
    if not product:
        messages.error(request,'selected product not found')
        return redirect('store')
    try:
        quantity = int(request.POST.get('quantity',1))
        if quantity <= 0:
            raise ValueError
    except (TypeError,ValueError):
        messages.error(request,'Enter a valid quantity.')
        return redirect('store')

    if product.stock < quantity:
        messages.error(request,f"Only {product.stock} item(s) available {product.name}.")
        return redirect('store')

    price = product.price
    try:
        discount_pct = Decimal(product.discount)/Decimal(100)
    except:
        discount_pct = Decimal(0)
    price_after_discount = (price * (Decimal(1)-discount_pct)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
    total_price = (price_after_discount * Decimal(quantity).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP))
    with transaction.atomic():
        order = Order.objects.create(customer=user,quantity=quantity,total_price=total_price)
        order.products.add(product)

        product.stock -= quantity
        product.save()
    messages.success(request,f"You ordered {quantity} x {product.name}")
    return redirect('store')








def add_to_cart_view(request):
    return redirect('store')

@customer_required
def order_page(request):
    return render(request,'order.html')
@customer_required
def cart_page(request):
    return render(request,'cart.html')
# Create your views here.

def subscribe_view(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        if mail:
            try:
                SubscribedUser.objects.create(mail=mail)
                messages.success(request,"Thank You for subscribing")
                return redirect('store')
            except IntegrityError:
                messages.success(request, "You're already subscribed!")
                return redirect('store')

