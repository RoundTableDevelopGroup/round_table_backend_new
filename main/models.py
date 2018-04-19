from django.db import models


class Channel(models.Model):
    # 频道名
    name = models.CharField(max_length=40)
    # 短名
    short = models.CharField(max_length=10)
    # 是否火
    hot = models.BooleanField(default=False)
