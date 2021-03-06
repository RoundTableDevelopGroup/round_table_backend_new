from django.db import models


class SiteImage(models.Model):
    # 图片
    img = models.ImageField(upload_to='img/site')
    # 创建时间
    time = models.DateTimeField(auto_now_add=True)


class UserImage(models.Model):
    # 图片
    img = models.ImageField(upload_to='img/user')
    # 创建时间
    time = models.DateTimeField(auto_now_add=True)


class ChannelType(models.Model):
    """
    频道类型
    """
    # 频道类别名
    name = models.CharField(max_length=20)
    # 缩写
    short = models.CharField(max_length=10)


class Channel(models.Model):
    """
    频道
    """
    # 频道名
    name = models.CharField(max_length=40)
    # 是否火
    hot = models.BooleanField(default=False)
    # 图片
    picture = models.IntegerField(default=0)
    # 描述
    description = models.CharField(max_length=200)
    # 类别id
    type = models.IntegerField()


class User(models.Model):
    """
    用户
    """
    # 用户名
    username = models.CharField(max_length=20)
    # 昵称
    nickname = models.CharField(max_length=32, blank=True)
    # 密码Hash
    password = models.CharField(max_length=64)
    # 盐
    salt = models.CharField(max_length=12)
    # 骑士id
    knight_id = models.CharField(max_length=8)
    # 管理员
    admin = models.BooleanField(default=False)
    # 头像图片 id
    avatar = models.IntegerField(default=0)
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True)
    # 性别
    sex = models.CharField(max_length=2, blank=True)
    # 手机号
    phone = models.CharField(max_length=20, blank=True)
    # 邮箱
    email = models.CharField(max_length=48, blank=True)
    # QQ
    qq = models.CharField(max_length=20, blank=True)
    # 微博
    weibo = models.CharField(max_length=20, blank=True)
    # 微信
    wechat = models.CharField(max_length=20, blank=True)
    # steam
    steam = models.CharField(max_length=20, blank=True)
    # 签名
    slogan = models.CharField(max_length=50, blank=True)


class UserAttentionChannel(models.Model):
    """
    用户关注频道关系
    """
    # 用户
    user = models.IntegerField()
    # 频道
    channel = models.IntegerField()


class Post(models.Model):
    """
    文章
    """
    # 标题
    title = models.CharField(max_length=100)
    # 作者 id
    author = models.IntegerField()
    # 频道 id
    channel = models.IntegerField()
    # 发表时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 最后修改时间
    modified_time = models.DateTimeField(auto_now=True)
    # 文章内容
    body = models.TextField()


class Comment(models.Model):
    """
    评论
    """
    # 发表者 id
    author = models.IntegerField()
    # 所在文章
    post = models.IntegerField()
    # 评论内容
    body = models.TextField()
    # 评论发表时间
    created_time = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    """
    回复
    """
    # 发表者 id
    author = models.IntegerField()
    # 回复者 id
    receiver = models.IntegerField()
    # 所属评论 id
    parent = models.IntegerField()
    # 回复内容
    body = models.TextField()
    # 回复发表时间
    created_time = models.DateTimeField(auto_now_add=True)


class UserLikePost(models.Model):
    """
    喜欢关系
    """
    # 用户 id
    user = models.IntegerField()
    # 文章 id
    post = models.IntegerField()


class Match(models.Model):
    """
    赛事
    """
    # 名字
    name = models.CharField(max_length=100)
    # 所属频道
    channel = models.IntegerField()
    # 描述
    description = models.TextField()
    # 报名开始日期
    sign_up_start_time = models.DateTimeField()
    # 报名结束日期
    sign_up_end_time = models.DateTimeField()
    # 比赛开始日期
    start_time = models.DateTimeField()
    # 比赛结束日期
    end_time = models.DateTimeField()


class UserJoinMatch(models.Model):
    """
    参与比赛关系
    """
    # 选手 id
    user = models.IntegerField()
    # 比赛 id
    match = models.IntegerField()
