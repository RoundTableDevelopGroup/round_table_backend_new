from main.models import User
from django.shortcuts import HttpResponse
import json
import time
import hashlib


# 骑士号生成器类
class KnightId:
    __vertex = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]

    @classmethod
    def generate(cls, username):
        """
        生成骑士id
        :param username: 用户名
        :return: 骑士id
        """
        # 将用户名和当前时间连接起来，构成骑士号种子
        torrent = username + str(time.time())
        # 获取种子的md5值
        md5_hash = hashlib.md5(torrent.encode('utf-8')).hexdigest()
        # 将MD5值每4位分组，求出4个数字的和并模36，并且经过骑士号转换矩阵构成骑士号的一位
        knight_id = ''
        tmp = 0
        for i in range(len(md5_hash)):
            tmp += int(md5_hash[i], 16)
            if i % 4 == 3:
                knight_id += cls.__vertex[tmp % 36]
                tmp = 0
        return knight_id


def get_login_state(request):
    # 从session获取内容
    if request.session.get('login_state'):
        return HttpResponse(json.dumps({
            'success': True
        }))
    else:
        return HttpResponse(json.dumps({
            'success': False
        }))


def register(request):
    # 获取参数
    params = json.loads(request.body)
    username = params.get('username')
    password = params.get('password')
    salt = params.get('salt')

    # 参数校验
    if (username and password and salt):
        # 先看用户名是否已经存在
        if (User.objects.filter(username=username).exists()):
            return HttpResponse(json.dumps({
                'success': False,
                'error_code': 200
            }))
        # 如果用户名不存在才能注册
        else:
            # 生成KnightID并且查重，如果有重复的KnightID则无限重复生成直到没有重复
            knight_id = KnightId.generate(username)
            while (User.objects.filter(knight_id=knight_id).exists()):
                knight_id = KnightId.generate(username)
            # 创建新用户
            user = User(
                username=username,
                password=password,
                salt=salt,
                knight_id=knight_id,
            )
            # 将用户存入数据库
            user.save()
            # 保存用户的登录信息到session
            request.session['login_state'] = True
            request.session['user_info'] = {
                'id': user.id
            }
            # 返回结果
            return HttpResponse(json.dumps({
                'success': True
            }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 100
        }))


def logout(request):
    # 将session重置
    request.session['login_state'] = False
    request.session['user_info'] = None
    # 返回结果
    return HttpResponse(json.dumps({
        'success': True
    }))


def get_salt(request):
    # 获取参数
    params = json.loads(request.body)
    username = params.get('username')
    # 参数校验
    if username:
        # 看用户名是否存在
        if User.objects.filter(username=username).exists():
            # 获取用户的盐并且返回
            return HttpResponse(json.dumps({
                'success': True,
                'salt': User.objects.get(username=username).salt
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


def login(request):
    # 获取参数
    params = json.loads(request.body)
    username = params.get('username')
    password = params.get('password')
    # 参数校验
    if username and password:
        # 先看用户名是否存在
        if User.objects.filter(username=username).exists():
            # 看用户名和密码哈希值是否匹配
            user = User.objects.get(username=username)
            if user.password == password:
                # 在session中保存用户的信息
                request.session['login_state'] = True
                request.session['user_info'] = {
                    'id': user.id
                }

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
                'error_code': 200
            }))
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 100
        }))
