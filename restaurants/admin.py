from django.contrib import admin
from restaurants.models import (
    RestaurantModel,
    MenuModel,
    DishModel,
    TypeOfDishModel,
    CuisineModel,
)


@admin.register(RestaurantModel)
class RastaurantModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    pass


@admin.register(DishModel)
class DishModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


@admin.register(TypeOfDishModel)
class TypeOfDishModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}



@admin.register(CuisineModel)
class CuisineModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}