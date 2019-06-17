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
        # user = authenticate(req, username=username, password=password)

        # 通过filter过滤函数通过字段筛选数据库库信息
        user = MyUser.objects.filter(username=username)

        # 判断用户信息是否在数据库中存在
        if user:
            # 用check_password判断数据库加密后的密码是否等于从前端接收过来密码
            if user[0].check_password(password):
                # 判断用户是否是激活状态
                if user[0].is_active:
                    # 使用django自带授权系统，如果授权成功返回user对象
                    user1 = authenticate(req, username=username, password=password)
                    # 在客户端存储cookie
                    login(req, user1)
                    # 判断cookie，session等信息
                    if user:
                        # 重定向到index界面
                        return redirect(reverse('polls:index'))
                else:
                    lf = MyUserLoginForm()
                    rf = MyUserRegisterForm()
                    errormessage = '账户未激活'
                    # 返回登陆注册界面
                    return render(req, 'polls/login_register.html', locals())
            else:
                lf = MyUserLoginForm()
                rf = MyUserRegisterForm()
                errormessage = '密码错误'
                # 返回登陆注册界面
                return render(req, 'polls/login_register.html', locals())
        else:
            lf = MyUserLoginForm()
            rf = MyUserRegisterForm()
            errormessage = '账户不存在'
            # 返回登陆注册界面
            return render(req, 'polls/login_register.html', locals())


class RegisterView(View):

    def post(self, req):
        try:
            username = req.POST.get('username')
            password = req.POST.get('password')
            email = req.POST.get('email')

            # 向数据库写入用户信息并查重
            user = MyUser.objects.create_user(username=username, email=email, password=password)

            # 将用户数据库中is_active中的默认值改为False，即为激活状态
            user.is_active = False
            # 因为改了字段的属性，所以需要重新保存
            user.save()

            # 引入发送邮件相关模块
            from django.core.mail import send_mail, EmailMultiAlternatives
            from django.conf import settings
            # 创建邮件信息，包括邮件标题，邮件内容，发送者，接收者
            mail = EmailMultiAlternatives(subject='激活账户',
                                   body='<h1><a href="http://127.0.0.1:8000/login/">点击激活账户</a></h1>',
                                   from_email=settings.DEFAULT_FROM_EMAIL,
                                   to=[email])
            # 设置文本格式
            mail.content_subtype = 'html'
            # 发送邮件
            mail.send()

            # 如果写入成功，则重定向至登陆界面
            if user:
                return redirect(reverse('polls:login'))
        except:
            lf = MyUserLoginForm()
            rf = MyUserRegisterForm()
            errormessage = '账户已存在，注册失败'
            return render(req, 'polls/login_register.html', locals())


class LogOutView(View):
    def get(self, req):
        logout(req)
        return redirect(reverse('polls:login'))


# class CheckUserName(View):
#     def get(self, req, id):
#         username = req.GET.get('')







"""
Http为无状态协议，每次请求之后都会断开链接
用户拿着用户名密码 请求数据 可以返回数据，当请求其他页面时，又要再次输入用户名密码
此时 常见做法 用户请求时会携带自身信息（服务端生成的信息） （Cookie）
Cookie就是用来保存用户身份的信息

"""
