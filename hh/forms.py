from django import forms
from hh.models import *
import os, sys
import datetime
import re
from django.forms import fields
from django.forms import widgets

class FM(forms.Form):
    '''
    这是用form  制作的验证
    '''
    email = fields.EmailField(error_messages={'required': '邮箱不能为空' ,'invalid':'邮箱格式错误'},
    widget = widgets.Input ( attrs={'name': 'email','onblur':'check_exist(this)'} ),

    )
    user_name = fields.CharField (
        error_messages={'required': '用户名不能为空.'},
        widget=widgets.Input (attrs={'name': 'user_name','onblur':'check_exist(this)'} ),
        label="用户名",
    )

    password  = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空.', 'min_length': '密码长度不能小于6', "max_length": '密码长度不能大于12'},
        widget=widgets.PasswordInput(attrs={'name': 'password','class': 'password','onblur':'confirmpass()'}),
        label="密码",

    )

    password2  = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空.', 'min_length': '密码长度不能小于6', "max_length": '密码长度不能大于12'},
        widget=widgets.PasswordInput(attrs={'name': 'password2','class': 'password2','onblur':'confirmpass()'}),
        label="确认密码",

    )

    class Meta:
        model = Users
        fields = ("user_name", "password","email")

    # 自定义方法（局部钩子），密码必须包含字母和数字
    def clean_password(self):
        if self.cleaned_data.get ( 'password' ).isdigit () or self.cleaned_data.get ( 'password' ).isalpha():
            raise forms.ValidationError ( '密码必须包含数字和字母' )
        else:
            return self.cleaned_data['password']

    # def clean_valid_code(self):  # 检验验证码正确；之前生成的验证码保存在了了session中
    #     if self.cleaned_data.get ( 'valid_code' ).upper () == self.request.session.get ( 'valid_code' ):
    #         return self.cleaned_data['valid_code']
    #     else:
    #         raise forms.ValidationError ( '验证码不正确' )

    # 自定义方法（全局钩子, 检验两个字段），检验两次密码一致;
    def clean(self):
        if self.cleaned_data.get ( 'password' ) != self.cleaned_data.get ( 'password2' ):
            raise forms.ValidationError ( '密码不一致' )
        else:
            return self.cleaned_data



class loginForm(forms.ModelForm):
    #生成两个密码input
    password = forms.CharField(widget=forms.PasswordInput, label="密码")
    password2 = forms.CharField(widget=forms.PasswordInput, label="确认密码")

    class Meta:
        model = Users
        fields = ("user_name", "password", )


class registerForm(forms.ModelForm):
    user_name = forms.CharField(required=True, error_messages={
        'required': '用户名不能为空',
    })
    email = forms.EmailField(error_messages={
        'required': '邮箱不能为空',
    })
    password = forms.CharField(widget=forms.PasswordInput, label="密码", error_messages={
        'required': '密码不能为空',
    })
    password2 = forms.CharField(widget=forms.PasswordInput, label="确认密码", error_messages={
        'required': '确认密码不能为空',
    })
    verify_code = forms.CharField(max_length=4, error_messages={
        'required': '验证码不能为空',
    })

    class Meta:
        model = Users
        fields = ("user_name", "password", "email")

    def clean_user_name(self):
        #用户名不能包含空格自定义校验
        cd = self.cleaned_data
        login_name = cd.get("user_name").strip()
        if "\s" in login_name:
            raise forms.ValidationError("用户名不能有空格")
        return login_name

    def clean_password2(self):
        #验证密码是否一致
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('密码和确认密码不一致')
        return cd['password2']
