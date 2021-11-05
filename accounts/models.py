from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from accounts.model_managers import CustomUserManager



class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    Custom model for users.
    """
    email = models.EmailField('email address', unique=True)
    user_name = models.CharField(max_length=250, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_restaurant = models.BooleanField(default=False)
    is_purchaser = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name
































