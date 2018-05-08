from main.models import Post, User, Channel, UserAttentionChannel
from django.db.models import Q
from django.shortcuts import HttpResponse
import json


def get_ten_channel_post(request):
    """
    获取10篇特定频道的文章
    """
    params = json.loads(request.body)
    channel = params.get('channel')
    last = params.get('last')
    # 参数校验
    if channel and last:
        # 查询数据库获取最后一条记录的下10条记录
        posts = Post.objects.filter(channel=channel).filter(id__gt=last).all()[0:10]
        l = []
        for post in posts:
            author = User.objects.get(id=post.author)
            channel = Channel.objects.get(id=post.channel)
            # 校验
            if author and channel:
                l.append({
                    'id': post.id,
                    'title': post.title,
                    'author': {
                        'id': author.id,
                        'nickname': author.nickname,
                        'slogan': author.slogan,
                        'avatar': author.avatar
                    },
                    'channel': {
                        'id': channel.id,
                        'name': channel.name
                    },
                    'created_time': post.created_time,
                    'modified_time': post.modified_time,
                    'body': post.body[0:100]
                })
            else:
                continue
        # 返回信息
        return HttpResponse(json.dumps({
            'success': True,
            'posts': l
        }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 100
        }))


def get_ten_index_channel_post(request):
    """
    获取10篇主页文章
    """
    params = json.loads(request.body)
    last = params.get('last')
    # 看用户是否登录
    login_state = request.session.get('login_state')
    if login_state:
        # 参数校验
        pass
    else:
        # 参数校验
        if last:
            # TODO
            pass
        else:
            return HttpResponse(json.dumps({
                'success': False,
                'error_code': 100
            }))