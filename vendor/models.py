from django.db import models
from django.conf import settings
class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    address = models.TextField(default='Unknown')

    def __str__(self):
        return self.shop_name
class Product(models.Model):
    vendor  = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits =10,decimal_places=2,default=0.0)
    discount = models.IntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.vendor.shop_name})"

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product,related_name='orders')
    quantity = models.IntegerField(null=False,blank=False)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"order #{self.customer.phone_number}"


# Create your models here.
