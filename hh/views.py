
# _*_ coding:utf-8 _*_
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response

import json
import time
from hh import models
#初始化数据库
from webconfig import web_config
from hh import forms as myforms
init_flag = web_config.init_check()
if init_flag == 'no':
    from models import init_database
    web_config.inited_db()
login_dict = {}



def homepage(request):
    '''
    主页
    :param request:
    :return:
    '''
    a = index(request)
    return a

def index(request):
    filename = 'index.html'
    catalog_name = []
    catalog_url = []
    data = models.Catalog.objects.all()
    obj = myforms.FM ( request.POST )
    r1 = obj.is_valid ()
    if r1:
        pass
    else:
        for d in data:
            if d.display_enabled: #当表的字段显示可用
                catalog_name.append(d.name)
                catalog_url.append(d.catalog_url)
            if catalog_name == []:
                catalog_name = ['数据库未初始化']
        return render(request,filename,{'obj': obj,'catalog_list': catalog_name ,'catalog_url':catalog_url})
    return render(request,filename,{'catalog_list': catalog_name ,'catalog_url':catalog_url})


def login(request):
    if request.method == "GET":
        # 从数据库中吧数据获取到
        pass


def auth(func):
    def inner(reqeust,*args,**kwargs):
        v = reqeust.COOKIES.get('username111')
        if not v:
            return redirect('/login/')
        return func(reqeust, *args,**kwargs)
    return inner

def check_userexist(request):
    # ajax验证是否用户名已经 注册
    '''
    check_type  前端的input 的 id 通过ajax 取值
    value  input 的 value
    :param request:
    :return:
    '''
    if request.method == 'POST':
        check_type = request.POST.get("check_type")
        value = request.POST.get("check_value")
        parameter = {check_type: value}
        count = models.Users.objects.filter(**parameter).count()
        if count > 0:
            return HttpResponse(json.dumps({'status': 'fail', 'msg': 'exist'}))
        else:
            return HttpResponse(json.dumps({'status': 'ok'}))

import hashlib
def register(request):
    '''
    注册，
    1.验证数据是否合法 ， 比如用户名是否包含空格，两次密码是否一致 ，必填字段是否为空。不合法返回form的自定义error
    2.
    :param request:
    :return:
    '''
    if request.method == 'POST':
        reg_check = myforms.FM(data=request.POST)
        if reg_check.is_valid():
            cd = reg_check.cleaned_data
            # 验证码比对
            # vcode_from_client = cd.get("verify_code", "")
            # vcode_in_session = request.session.get("verify_code")
            # if vcode_from_client and vcode_in_session and vcode_from_client.upper() == vcode_in_session.upper():
            #     # 验证码比对通过
            if True:
                #写入数据库
                new_user = reg_check.save(commit=False)
                password2 = cd.get("password2")
                m = hashlib.md5()
                m.update(password2.encode())
                new_user.password = m.hexdigest()
                new_user.display_name = cd.get("login_name")
                new_user.email = cd.get("email")
                new_user.last_login = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                new_user.last_ip = request.META.get("REMOTE_ADDR")
                new_user.save()
                return HttpResponse(json.dumps({'status': 'ok'}))
            return HttpResponse(json.dumps({'status': 'fail', 'msg': '验证码不正确'}))
        else:
            return HttpResponse(reg_check.errors.as_json())

