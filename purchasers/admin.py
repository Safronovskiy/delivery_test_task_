from django.contrib import admin
from purchasers.models import (
    PurchaserModel,
    PurchaserAddressModel,
    PurchaserCardModel,
)


@admin.register(PurchaserModel)
class PurcharesModelAdmin(admin.ModelAdmin):
    pass


@admin.register(PurchaserAddressModel)
class PurcharesaAddressModelAdmin(admin.ModelAdmin):
    pass


@admin.register(PurchaserCardModel)
class PurcharesCardModelAdmin(admin.ModelAdmin):
    pass