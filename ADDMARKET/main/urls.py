from django.contrib.auth.views import LoginView
from django.urls import path
from .views import RegisterView
from . import views
urlpatterns = [
    path('index', views.index),
    path('', views.index),
    path('about', views.about),
    path('contacts', views.contacts),
    path('twitch', views.twitch),
    path('telegram', views.telegram),
    path('tv', views.tv),
    path('vk', views.vk),
    path('youtube', views.youtube),
    path('profile', views.profile, name='profile'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('ads', views.news_home, name="news_home"),
    path('create', views.create, name="create"),
    path('print_telegram', views.print_telegram),
    path('print_tv', views.print_tv),
    path('print_youtube', views.print_youtube),
    path('print_vk', views.print_vk),
    path('print_twitch', views.print_twitch),
]
