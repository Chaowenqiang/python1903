from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from .models import Question,Choice,MyUser
from .forms import MyUserLoginForm,MyUserRegisterForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

"""
视图两种写法  第一种 视图函数  第二种叫做视图类

"""

# def index(req):
#     return render(req,"polls/index.html")

"""
在视图模块声明 视图函数  index，这个函数有系统调用
应为：我们将路由与视图函数绑定了
当我们输入的网址和某一个路由匹配成功，就会调用该路由绑定的视图函数
在调用该函数时 会将请求（req）以及参数列表传给给该函数
"""


def checklogin(fun):
    def check(self,req,*args):
        if req.user and req.user.is_authenticated:
            return fun(self,req,*args)
        else:
            return redirect(reverse("polls:login"))
    return check


class IndexView(View):
    """
    通过重写父类View实现完成通用视图类的功能
    重写get方法代表重写get请求
    """
    @checklogin
    def get(self,req):
        print("----")
        print(req)
        questions = Question.objects.all()
        return render(req, "polls/index.html", locals())


class DetailView(View):
    @checklogin
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req, "polls/detail.html", locals())

    @checklogin
    def post(self,req,id):
        c_id = req.POST.get("info")
        choice = Choice.objects.get(pk=c_id)
        choice.vites += 1
        choice.save()
        # return render(req, 'polls/result.html', locals())
        return redirect(reverse("polls:result", args=(id, )))


class ReusltView(View):
    @checklogin
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req,"polls/result.html",locals())


class LoginView(View):

    # 定义get请求函数
    def get(self,req):
        lf = MyUserLoginForm()
        rf = MyUserRegisterForm()
        return render(req, "polls/login_register.html", locals())

    # 定义post请求函数
    def post(self,req):

        # 获取post请求所得到的值
        username = req.POST.get("username")
        password = req.POST.get("password")

        # 使用django自带授权系统，如果授权成功返回user
        user = authenticate(req, username=username, password=password)
        # 判断用户信息是否在数据库中存在
        if user:
            # 在客户端存储cookie
            login(req, user)
            # 重定向到index界面
            return redirect(reverse('polls:index'))
        else:
            lf = MyUserLoginForm()
            rf = MyUserRegisterForm()
            errormessage = '登陆失败'
            # 返回登陆注册界面
            return render(req, 'polls:login_register.html', locals())


class RegisterView(View):

    def post(self, req):
        try:
            username = req.POST.get('username')
            password = req.POST.get('password')
            email = req.POST.get('email')

            # 向数据库写入用户信息并查重
            user = MyUser.objects.create_user(username=username, email=email,password=password)
            # 如果写入成功，则重定向至登陆界面
            if user:
                return redirect(reverse('polls:index'))
        except:
            lf = MyUserLoginForm()
            rf = MyUserRegisterForm()
            errormessage = '账户已存在，注册失败'
            return render(req, 'polls/login_register.html', locals())


class LogOutView(View):
    def get(self, req):
        logout(req)
        return redirect(reverse('polls:login'))








"""
Http为无状态协议，每次请求之后都会断开链接
用户拿着用户名密码 请求数据 可以返回数据，当请求其他页面时，又要再次输入用户名密码
此时 常见做法 用户请求时会携带自身信息（服务端生成的信息） （Cookie）
Cookie就是用来保存用户身份的信息

"""
