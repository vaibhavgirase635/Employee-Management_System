from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, default=False)
    email = models.EmailField(unique=True)
    
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    Location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    Last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self):
        return "%s %s %s " %(self.first_name,self.Last_name,self.phone)

