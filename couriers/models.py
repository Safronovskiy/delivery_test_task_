from django.db import models
from accounts.models import UserModel
from cart.models import OrderModel



class CourierModel(models.Model):
    """ ... """
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    orders = models.ManyToManyField(OrderModel, blank=True)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
