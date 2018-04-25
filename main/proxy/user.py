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
    username = request.POST.get('username')
    password = request.POST.get('password')
    salt = request.POST.get('salt')
    # 参数校验
    if (username and password and salt):
        # 将数据存入数据库
        user = User(
            username=username,
            password=password,
            salt=salt,
            knight_id=KnightId.generate(username),
        )
        user.save()

        # 在session中储存用户信息
        request.session['login_state'] = True
        request.session['user_info'] = {
            id: user.id
        }
    else:
        return HttpResponse(json.dumps({
            'success': False,
            'error_code': 0
        }))