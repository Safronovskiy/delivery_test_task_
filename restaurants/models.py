from django.db import models
from accounts.models import UserModel


class RestaurantModel(models.Model):
    """ ... """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    address = models.TextField(max_length=250)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class MenuModel(models.Model):
    """ ... """
    restaurant = models.ForeignKey(RestaurantModel,  on_delete=models.CASCADE)
    cuisine = models.ForeignKey('CuisineModel', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    dishes = models.ManyToManyField('DishModel', related_name='menus')
    description = models.TextField(max_length=1000, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class DishModel(models.Model):
    """ ... """
    type = models.ForeignKey('TypeOfDishModel', related_name='dishes', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(max_length=1250, blank=True, null=True)
    image = models.ImageField(upload_to='dishes_imgs/%Y/%m/', blank=True, null=True)
    cooking_time = models.PositiveIntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=True)
    is_special_offer = models.BooleanField(default=False)
    is_hit = models.BooleanField(default=False)
    owner = models.ForeignKey(UserModel, related_name='owner_dish', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class TypeOfDishModel(models.Model):
    """ ... """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    title_image = models.ImageField(upload_to='dishtype_imgs/%Y/%m/', blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class CuisineModel(models.Model):
    """ ... """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


