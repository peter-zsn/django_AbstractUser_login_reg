#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: models.py
@time: 2017/7/27 11:44
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(u'用户姓名', max_length=10)
    relpwd = models.IntegerField(u'明文密码')
    # password = models.IntegerField(u'明文密码')

    class Meta:
        db_table = 'user'

class UserInfo(models.Model):
    user = models.ForeignKey(User)          # 用户id
    sex = models.IntegerField(u'性别')      # 1 男 2女
    home = models.CharField(u'住址', max_length=255)  # 住址
    company = models.CharField(u'公司', max_length=255)   # 公司

    class Meta:
        db_table = 'user_info'