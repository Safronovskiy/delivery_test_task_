from django.contrib import admin
from accounts.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    pass


