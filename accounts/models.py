from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class CustomUserManager(BaseUserManager):
    """ Manager for CustomUser. Implements create_user and create_superuser"""
    def create_user(self,Phone_number,role,Password=None,**extra_fields):
        if not Phone_number:
            raise ValueError("Phone number is required.")
        phone_number = str(Phone_number).strip()
        user = self.model(phone_number=phone_number,role=role,**extra_fields)
        user.set_password(Password)
        user.save(using=self._db)
        return user
    def create_superuser(self,phone_number,password,**extra_fields):
        """ Creates and saves a superuser with the given phone_number and passwords"""
        if not password:
            raise ValueError('Superuser must have a Password.')
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields['role'] = None

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must  have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(phone_number,password,**extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone_number = models.CharField(max_length=15,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6,blank=True,null=True)
    otp_created_at = models.DateTimeField(blank=True,null=True)
    otp_used = models.BooleanField(default=False)
    ROLE_CHOICES = (('vendor','Vendor'),('customer','Customer'),)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
    def is_vendor(self):
        return self.role == 'vendor'
    def is_customer(self):
        return self.role == 'customer'
