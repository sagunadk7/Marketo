from django.contrib import admin
from .models import SubscribedUser

@admin.register(SubscribedUser)
class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ['mail','created_at']
    search_fields = ['mail']
# Register your models here.
