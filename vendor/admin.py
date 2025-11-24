from django.contrib import admin
from vendor.models import Vendor, Product,Order

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=('user','shop_name','address')
@admin.register(Product)
class ItemDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id','vendor','name','price','discount','stock']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','created_at','get_products','total_price']
    def get_products(self,obj):
        return ", ".join([p.name for p in obj.products.all()])
    get_products.short_description = 'Product'

# Register your models here.
