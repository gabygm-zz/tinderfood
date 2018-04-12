from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, null=False, related_name='client_profile', db_index=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='avatar/')


class DishFood(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    likes = models.PositiveSmallIntegerField(default=0)
    description = models.CharField(blank=True, null=True, max_length=5000)


class ClientListFood(models.Model):
    name = models.CharField(max_length=150, blank=True, db_index=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #TODO default list favorites dish food


class ListItem(models.Model):
    item = models.ForeignKey(DishFood, null=True, blank=True, db_index=True, on_delete=models.SET_NULL)
    list = models.ForeignKey(ClientListFood, null=True, related_name="items", db_index=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)