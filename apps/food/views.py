from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.food.models import DishFood, ClientListFood, Client, ListItem

@login_required()
def home(request):
    context = {'dishes': DishFood.objects.all()}
    return render(request, 'home.html', context=context)


class FishFoodLikeView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def put(self, request, fish_id):
        try:
            dish_food = DishFood.objects.get(id=fish_id)
            client = Client.objects.get(user=self.request.user)
        except ObjectDoesNotExist:
            return Response({"error": "No DishFood with that ID found"}, status=status.HTTP_404_NOT_FOUND)

        dish_food.likes += 1
        dish_food.save()
        obj, created = ClientListFood.objects.get_or_create(name="favorite_dishes", client=client)
        obj, created = ListItem.objects.get_or_create(list=obj, item=dish_food)
        obj.item = dish_food
        obj.save()

        return Response('liked', status=status.HTTP_200_OK)


class Dashboard(generic.TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        client = Client.objects.get(user=self.request.user)
        context = super(Dashboard, self).get_context_data()

        context['popular_products'] = DishFood.objects.all().order_by('-likes')

        categories_favorites = ClientListFood.objects.filter(name="favorite_dishes", client=client).first()
        clients = []
        all_client = Client.objects.all()
        for client in all_client:
            cat = []
            categories_favorites = ClientListFood.objects.filter(name="favorite_dishes", client=client).first()
            for favorites in categories_favorites.items.all().order_by('-updated_at'):
                cat.append(favorites.item.category.name)
            clients.append({'client': client, 'category': cat})

        categories = []
        for favorites in categories_favorites.items.all().order_by('-updated_at'):
            categories.append(favorites.item.category)

        context['clients_favorite_food'] = categories
        context['clients'] = clients
        return context