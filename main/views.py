from .proxy import channel
from .proxy import user


def channel__get_all_channel(request):
    return channel.get_all_channel(request)


def channel__get_hot_channel(request):
    return channel.get_hot_channel(request)

def user__get_login_state(request):
    return user.get_login_state(request)

def user__register(request):
    return user.register(request)

def user__logout(request):
    return user.logout(request)
