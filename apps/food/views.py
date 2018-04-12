from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.food.models import DishFood, ClientListFood, Client, ListItem


class FishFoodLikeView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def put(self, request, fish_id):
        try:
            dish_food = DishFood.objects.get(id=fish_id)
            client = Client.objects.get(user=self.request.user)
        except ObjectDoesNotExist:
            return Response({"error": "No DishFood with that ID found"}, status=status.HTTP_404_NOT_FOUND)
        if dish_food.likes > 0:
            dish_food.likes += 1
            dish_food.save()
        obj, created = ClientListFood.objects.get_or_create(name="favorite_dishes", client=client)
        item, created = ListItem.objects.get_or_create(list=obj, item=fish_id)

        return Response('liked', status=status.HTTP_200_OK)