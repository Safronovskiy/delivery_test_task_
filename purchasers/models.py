from django.db import models
from accounts.models import UserModel


class PurchaserModel(models.Model):
    """ ... """
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    second_name = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='purchaser_imgs/%Y/%m', blank=True, null=True)
    phone = models.CharField(max_length=250)

    class Meta:
        ordering = ('second_name',)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first_name.capitalize()} {self.second_name.capitalize()} '



class PurchaserAddressModel(models.Model):
    """ ... """
    purchaser = models.ForeignKey(PurchaserModel, related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    post_index = models.CharField(max_length=100)

    class Meta:
        ordering = ('city',)

    def __str__(self):
        return self.full_address()

    def full_address(self):
        return f'{self.city}, {self.street} st., {self.house} - {self.room}'



class PurchaserCardModel(models.Model):
    """ ... """
    purchaser = models.ForeignKey(PurchaserModel, related_name='card', on_delete=models.CASCADE)
    number = models.CharField(max_length=250)
    secret_code = models.CharField(max_length=250)
    expire_date = models.DateField()
    owner_name = models.CharField(max_length=250)
    issuing_bank = models.CharField(max_length=250)

    class Meta:
        ordering = ('owner_name',)

    def __str__(self):
        return f'{self.owner_name}, card: {self.number[:4]}'

