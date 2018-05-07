from main.models import Channel, SiteImage, ChannelType, UserAttentionChannel
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
            picture = SiteImage.objects.get(id=channel.picture)
            if picture:
                type = ChannelType.objects.get(id=channel.type)
                if type:
                    return HttpResponse(json.dumps({
                        'success': True,
                        'name': channel.name,
                        'hot': channel.hot,
                        'picture': picture.img.url,
                        'description': channel.description,
                        'type': type.short
                    }))
                else:
                    return HttpResponse(json.dumps({
                        'success': False,
                        'error_code': 202
                    }))
            else:
                return HttpResponse(json.dumps({
                    'success': False,
                    'error_code': 201
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


def user_attention_channel(request):
    params = json.loads(request.body)
    channel = params.get('channel')
    login_state = request.session.get('login_state')
    user = None
    if login_state:
        user = request.session.get('user_info').get('id')
        # 参数校验
        if channel and user:
            # 先看用户是否已经关注过该频道了
            if UserAttentionChannel.objects.filter(
                user=user,
                channel=channel
            ):
                return HttpResponse(json.dumps({
                    'success': False,
                    'error_code': 202
                }))
            else:
                # 将关系存入数据库
                tmp = UserAttentionChannel(
                    user=user,
                    channel=channel
                )
                tmp.save()
                return HttpResponse(json.dumps({
                    'success': True
                }))
        else:
            return HttpResponse(json.dumps({
                'success': False,
                'error_code': 100
            }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 201
        }))
