from django import forms
from .models import MyUser


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
        # widget = {'username':forms.TextInput(attrs={'placeholder':'请输入用户名'})}

class MyUserRegisterForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = ['username', 'password', 'email']