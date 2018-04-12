from django.contrib import admin
from django.urls import path
from apps.food import views as foodviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', foodviews.home, name='home'),

]
