from django.urls import path
from . import views

urlpatterns = [
    path('channel/get_all_channel', views.channel__get_all_channel),
    path('channel/get_hot_channel', views.channel__get_hot_channel)
]