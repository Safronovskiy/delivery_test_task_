from django.contrib import admin
from cart.models import (
    CartModel,
    CartDishModel,
    OrderStatusModel,
)


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    pass

@admin.register(CartDishModel)
class CartDishModelAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderStatusModel)
class OrderStatusModelAdmin(admin.ModelAdmin):
    pass











