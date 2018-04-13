from django.contrib import admin

# Register your models here.
from apps.food.models import Client, DishFood, ClientListFood, ListItem, Category


class DishFoodAdmin(admin.ModelAdmin):
    readonly_fields = ['likes']
    list_display = ['name', 'description']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

#admin.site.register(Client)
admin.site.register(DishFood, DishFoodAdmin)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(ClientListFood)
#admin.site.register(ListItem)