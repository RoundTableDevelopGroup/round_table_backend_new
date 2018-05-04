from .proxy import channel
from .proxy import user
from .proxy import file


def channel__get_all_channel(request):
    return channel.get_all_channel(request)


def channel__get_hot_channel(request):
    return channel.get_hot_channel(request)


def channel__get_channel_info_by_id(request):
    return channel.get_channel_info_by_id(request)


def user__get_login_state(request):
    return user.get_login_state(request)


def user__register(request):
    return user.register(request)


def user__logout(request):
    return user.logout(request)


def user__get_salt(request):
    return user.get_salt(request)


def user__login(request):
    return user.login(request)


def file__image_upload(request):
    return file.image_upload(request)
