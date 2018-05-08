from main.models import Channel, SiteImage, ChannelType, UserAttentionChannel, Post
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
    """
    关注频道
    """
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
            ).exists():
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


def user_un_attention_channel(request):
    """
    用户取消关注频道
    """
    params = json.loads(request.body)
    channel = params.get('channel')
    login_state = request.session.get('login_state')
    if login_state:
        user = request.session.get('user_info').get('id')
        # 参数校验
        if user and channel:
            # 看用户是否已经关注了该频道
            if UserAttentionChannel.objects.filter(
                user=user,
                channel=channel
            ).exists():
                UserAttentionChannel.objects.get(
                    user=user,
                    channel=channel
                ).delete()
                return HttpResponse(json.dumps({
                    'success': True
                }))
            else:
                return HttpResponse(json.dumps({
                    'success': False,
                    'error_code': 201
                }))
        else:
            return HttpResponse(json.dumps({
                'success': False,
                'error_code': 100
            }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 200
        }))


def is_user_attention_the_channel(request):
    """
    用户是否关注了特定的频道
    """
    # 获取参数
    params = json.loads(request.body)
    channel = params.get('channel')
    # 看用户是否登录
    login_state = request.session.get('login_state')
    if login_state:
        user = request.session.get('user_info').get('id')
        # 参数校验
        if user and channel:
            # 查询数据库
            if UserAttentionChannel.objects.filter(
                user=user,
                channel=channel
            ).exists():
                return HttpResponse(json.dumps({
                    'success': True,
                    'attention': True
                }))
            else:
                return HttpResponse(json.dumps({
                    'success': True,
                    'attention': False
                }))
        else:
            return HttpResponse(json.dumps({
                'success': False,
                'error': 100
            }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 200
        }))


def get_channel_attention_num(request):
    """
    获取频道关注数
    """
    params = json.loads(request.body)
    channel = params.get('channel')
    # 参数校验
    if channel:
        # 获取数据库中查询关注数量
        num = UserAttentionChannel.objects.filter(
            channel=channel
        ).count()
        # 看这个关注量处于哪一个数量级
        if num >= 10000:
            return HttpResponse(json.dumps({
                'success': True,
                'num': str(format(float(num) / float(10000), '.1f') + 'W')
            }))
        else:
            if num >= 1000:
                return HttpResponse(json.dumps({
                    'success': True,
                    'num': str(format(float(num) / float(1000), '.1f') + 'K')
                }))
            else:
                return HttpResponse(json.dumps({
                    'success': True,
                    'num': str(num)
                }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 100
        }))


def get_channel_hot_degree(request):
    params = json.loads(request.body)
    channel = params.get('channel')
    # 参数校验
    if channel:
        # 查询数据库获取频道热度
        num = Post.objects.filter(
            channel=channel
        ).count()
        # 根据num的数量级做出不同的响应
        if num >= 10000:
            return HttpResponse(json.dumps({
                'success': True,
                'num': str(format(float(num) / float(10000), '.1f') + 'W')
            }))
        else:
            if num >= 1000:
                return HttpResponse(json.dumps({
                    'success': True,
                    'num': str(format(float(num) / float(1000), '.1f') + 'K')
                }))
            else:
                return HttpResponse(json.dumps({
                    'success': True,
                    'num': str(num)
                }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 100
        }))