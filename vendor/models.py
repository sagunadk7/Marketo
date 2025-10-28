from django.db import models
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=30)


    def __str__(self):
        return self.vendor_name
class ItemsDescription(models.Model):
    vendor  = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    item_name = models.CharField(max_length=20)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.item_name

class Orders(models.Model):
    order_by = models.CharField(max_length=20)
    order_at = models.DateField(auto_now_add=True)
    item_name = models.CharField(max_length=20)
    quantity = models.IntegerField(null=False,blank=False)



# Create your models here.
