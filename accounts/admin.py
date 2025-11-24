from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('phone_number','is_staff','is_superuser','is_active')
    search_fields = ('phone_number',)
    list_filter = ("is_staff","is_superuser","is_active")
    ordering = ("phone_number",)
    filter_horizontal = ("groups","user_permissions")
    fieldsets = (
    (None,{'fields':('phone_number','password')}),
    ('permissions',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )
    add_fieldsets = (
    (None, {
        'classes':('wide',),
        'fields': ('phone_number','role','password1','password2',"is_staff", "is_superuser", "is_active"),
    }),
    )
# Register your models here.
