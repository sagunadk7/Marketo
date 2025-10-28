from django.contrib import admin
from vendor.models import Vendor, ItemsDescription,Orders

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=('id','vendor_name')
@admin.register(ItemsDescription)
class ItemDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id','vendor','item_name','price','discount')
@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','order_by', 'order_at','item_name','quantity']

# Register your models here.
