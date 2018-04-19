from main.models import Channel
from django.shortcuts import HttpResponse
import json


def get_all_channel(request):
    # 查询数据库
    result = Channel.objects.all()
    data = []
    for item in result:
        data.append({
            'name': item.name,
            'short': item.name,
            'hot': item.hot
        })
    return HttpResponse(json.dumps(data))
