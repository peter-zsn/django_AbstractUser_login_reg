#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: views.py
@time: 2017/7/27 11:36
"""

from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
import datetime


from libs.common.render_tmp import render_template
from libs.models.account.models import User, UserInfo


def index(request):
    data = {}
    return render_template(request, 'common.html', data)

def user_login(request):
    data = {
    }
    if request.method == 'POST':
        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            if not username or not password:
                return HttpResponse(u'请输入用户名和密码')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponse(u'登陆成功')
            else:
                return HttpResponse(u'账号密码错误')
        except Exception, e:
            print e
            return HttpResponse(u'账号密码错误')
    return render_template(request, 'login.html', data)

def user_reg(request):
    data = {
    }
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        sex = request.POST.get('sex', '')
        home = request.POST.get('home', '')
        company = request.POST.get('company', '')
        if not (username and password and sex and home and company):
            return HttpResponse(u'请完善信息')
        user = User.objects.filter(name=username).all()
        if user:
            return HttpResponse(u'已注册')
        else:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            relpwd=password,
                                            name=username,
                                            last_login=datetime.datetime.now())
            user_info = UserInfo.objects.create(user_id=user.id, sex=sex, home=home, company=company)
            if user_info:
                str = u'你的账号是:%s 密码是: %s' % (user.name, user.relpwd)
                return HttpResponse(str)
            else:
                return HttpResponse(u'注册失败')
    return render_template(request, 'reg.html', data)