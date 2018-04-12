from django.contrib import admin

# Register your models here.
from apps.food.models import Client, DishFood, ClientListFood, ListItem

class DishFoodAdmin(admin.ModelAdmin):
    readonly_fields = ['likes']
    list_display = ['name', 'description']

#admin.site.register(Client)
admin.site.register(DishFood, DishFoodAdmin)
#admin.site.register(ClientListFood)
#admin.site.register(ListItem)