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


def get_channel_info_by_id(request):
    # 获取参数
    params = json.loads(request.body)
    channel_id = params.get('id')
    if channel_id:
        # 查询频道
        channel = Channel.objects.get(
            id=channel_id
        )
        if channel:
            return HttpResponse(json.dumps({
                'success': True,
                'name': channel.name,
                'hot': channel.hot,
                'picture': channel.picture
            }))
        else:
            return HttpResponse(json.dumps({
                'success': False,
                'error_code': 200
            }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 100
        }))