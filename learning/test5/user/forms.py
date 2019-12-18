import re
import hashlib
from django import forms
from .models import *
from captcha.fields import CaptchaField
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def hash_code(s, salt='myuser'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

class UserRegisterForm(forms.ModelForm):
    cpwd =forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'cpwd',
            'email'
        ]
        labels = {
            'username': '用户名',
            'password': '密码',
            'email': '邮箱',
        }
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('cpwd')
        email = self.cleaned_data.get('email')

        if username and password1 and password2 and email:
            if password1 != password2:
                raise forms.ValidationError('两次输入的密码不同')

            if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
                raise forms.ValidationError('邮箱格式不正确')

            user_qs = User.objects.filter(username=username)
            if user_qs.exists():
                raise forms.ValidationError('用户名已经存在')

            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError('该邮箱已经被注册了！')
        return super(UserRegisterForm, self).clean(*args, **kwargs)

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'name_input', 'placeholder': "请输入用户名"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pass_input', 'placeholder': '请输入密码'}))
    captcha = CaptchaField(label='验证码')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = hash_code(self.cleaned_data.get('password'))
        captcha = self.cleaned_data.get('captcha')

        if username and password and captcha:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('用户名或密码错误')
        return super(UserLoginForm, self).clean(*args, **kwargs)

