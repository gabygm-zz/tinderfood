from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from apps.food import views as foodviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', foodviews.home, name='home'),
    url(r'^liked/(?P<fish_id>.+)/$', staff_member_required()(foodviews.FishFoodLikeView.as_view()), name="liked"),

]
