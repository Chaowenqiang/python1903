from django import forms
from .models import MyUser
from django.utils.translation import gettext_lazy


# class LoginForm(forms.Form):
#     # 定义表单中的邮件字段
#     email = forms.EmailField(label="邮箱", widget=forms.EmailInput(
#         attrs={"id": "email", "class": "form-control", "placeholder": "请输入邮箱"}))
#
#     username = forms.CharField(label="用户名", max_length=15, min_length=6, widget=forms.TextInput(
#         attrs={"id": "username", "class": "form-control", "placeholder": "请输入用户名"}))
#
#     password = forms.CharField(label="密码", max_length=6, min_length=6, widget=forms.PasswordInput(
#         attrs={'id': 'password', 'class': 'form-control', 'placeholder': '请输入密码'}))


class MyUserLoginForm(forms.ModelForm):
    '''
    由模型生成表单类,重写models模型中的部分字段即可
    '''
    class Meta():
        model = MyUser
        fields = ['username', 'password']
        # 重写字段样式
        widgets = {"password": forms.PasswordInput(attrs={"class": "form-control"}),
                   "username": forms.TextInput(attrs={"class": "form-control"})
                   }
        help_texts = {
            "username": gettext_lazy(""),
        }


class MyUserRegisterForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = ['username', 'password', 'email']
        # 重写字段样式
        widgets = {"password": forms.PasswordInput(attrs={"class": "form-control"}),
                   "username": forms.TextInput(attrs={"class": "form-control"}),
                   "email": forms.EmailInput(attrs={"class": "form-control"})
                   }
        help_texts = {
            "username": gettext_lazy(""),
        }