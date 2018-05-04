from django.urls import path
from . import views

urlpatterns = [
    path('channel/get_all_channel', views.channel__get_all_channel),
    path('channel/get_hot_channel', views.channel__get_hot_channel),
    path('channel/get_channel_info_by_id', views.channel__get_channel_info_by_id),

    path('user/get_login_state', views.user__get_login_state),
    path('user/register', views.user__register),
    path('user/logout', views.user__logout),
    path('user/get_salt', views.user__get_salt),
    path('user/login', views.user__login),

    path('file/image_upload', views.file__image_upload)
]
