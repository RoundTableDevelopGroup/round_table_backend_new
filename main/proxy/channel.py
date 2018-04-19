from main.models import Channel
from django.shortcuts import HttpResponse
import json


def get_all_channel(request):
    data = []
    for item in Channel.objects.all():
        data.append({
            'id': item.id,
            'name': item.name,
            'hot': item.hot
        })
    return HttpResponse(json.dumps(data))


def get_hot_channel(request):
    data = []
    for item in Channel.objects.all():
        if item.hot:
            data.append({
                'id': item.id,
                'name': item.name
            })
    return HttpResponse(json.dumps(data))
