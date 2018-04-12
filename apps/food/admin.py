from django.contrib import admin

# Register your models here.
from apps.food.models import Client, DishFood, ClientListFood, ListItem

admin.site.register(Client)
admin.site.register(DishFood)
admin.site.register(ClientListFood)
admin.site.register(ListItem)