from .proxy import channel


def channel__get_all_channel(request):
    return channel.get_all_channel(request)


def channel__get_hot_channel(request):
    return channel.get_hot_channel(request)
