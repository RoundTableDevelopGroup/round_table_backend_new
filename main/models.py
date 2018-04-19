from django.db import models


class Channel(models.Model):
    # 频道名
    name = models.CharField(max_length=40)
    # 是否火
    hot = models.BooleanField(default=False)


class User(models.Model):
    # 用户名
    username = models.CharField(max_length=32)
    # 密码Hash
    password = models.CharField(max_length=64)
    # 盐
    salt = models.CharField(max_length=12)
    # 骑士id
    knight_id = models.CharField(max_length=8)
    # 管理员
    admin = models.BooleanField(default=False)
    # 头像
    avatar = models.CharField(max_length=100, blank=True)
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True)
    # 性别
    sex = models.CharField(max_length=2, blank=True)
    # 手机号
    phone = models.CharField(max_length=20, blank=True)
    # 邮箱
    email = models.CharField(max_length=48, blank=True)
    # 关注频道
    channel = models.CharField(max_length=100, blank=True)
    # QQ
    qq = models.CharField(max_length=20, blank=True)
    # 微博
    weibo = models.CharField(max_length=20, blank=True)
    # 微信
    wechat = models.CharField(max_length=20, blank=True)
    # steam
    steam = models.CharField(max_length=20, blank=True)
