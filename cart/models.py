from django.db import models
from restaurants.models import DishModel, RestaurantModel
from purchasers.models import PurchaserModel, PurchaserAddressModel



class CartModel(models.Model):
    """ ... """
    purchaser = models.ForeignKey(PurchaserModel, related_name='my_carts', on_delete=models.CASCADE)
    orders = models.ManyToManyField('OrderModel', blank=True)

    def __str__(self):
        return f'Cart of: {self.purchaser.full_name()}'


class CartDishModel(models.Model):
    """ ... """
    purchaser = models.ForeignKey(PurchaserModel, on_delete=models.CASCADE)
    dish = models.ForeignKey(DishModel, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField('Price for 1 unit', max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Cart dish: {self.dish.title}'

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.dish.price
        if not self.total_price:
            self.total_price = self.price * self.amount
        super().save(*args, **kwargs)



class OrderModel(models.Model):
    """ ... """
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    purchaser = models.ForeignKey(PurchaserModel, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(CartDishModel, blank=True)
    status = models.ForeignKey('OrderStatusModel', on_delete=models.SET_NULL, blank=True, null=True) # когда заказ содался статус должен быть new
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    deliver_from = models.CharField(max_length=250, blank=True)
    delver_to = models.CharField(max_length=250, blank=True)
    order_total_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    purchaser_appeal = models.TextField(max_length=2000, blank=True, null=True)                           # возможно переделать на FK
    pay_cash = models.BooleanField(default=True)
    pay_card = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        # проверить установлен ли статус, если нет тогда создать new и установить каждому новому заказу
        if not self.status:
            new, _ = OrderStatusModel.objects.get_or_create(status_name='New')
            self.status = new
        if not self.deliver_from:
            self.deliver_from = self.restaurant.address
        if not self.delver_to:
            self.deliver_to = self.purchaser.address.first().full_address()
        if not self.order_total_price:
            price = sum([dish.total_price for dish in self.dishes.all()])
            self.total_order_price = price
        super().save(*args, **kwargs)


class OrderStatusModel(models.Model):
    """ ... """
    status_name = models.CharField(max_length=100)
