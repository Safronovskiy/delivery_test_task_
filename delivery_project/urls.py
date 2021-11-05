from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('api/accounts/', include('accounts.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/couriers/', include('couriers.urls')),
    path('api/purchasers/', include('purchasers.urls')),
    path('api/restaurants/', include('restaurants.urls')),

    path('admin/', admin.site.urls),

]
