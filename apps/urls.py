from django.contrib import admin
from django.urls import path
from apps.food import views as foodviews


urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^client_profile/fish_food/(?P<id>.+)/like/$',foodviews ..as_view(),
    #    name="client_check_favorite"),

]
