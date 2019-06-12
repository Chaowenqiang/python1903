from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from .models import Question,Choice
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
        if req.COOKIES.get("username"):
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
        return redirect(reverse("polls:result", args=(id, )))

class ReusltView(View):
    @checklogin
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req,"polls/result.html",locals())

class LoginView(View):
    def get(self,req):
        return render(req,"polls/login.html")

    def post(self,req):
        username = req.POST.get("username")
        pwd = req.POST.get("password")
        # 查询数据库是否有该用户，如果有则登录成功，跳转到首页  需要设置Cookie
        # cookie实在response里设置
        res = redirect(reverse("polls:index"))
        res.set_cookie("username",username)
        return res




# def mylog(info):
#     print(info)
#
# mylog("helloworld")


"""
Http为无状态协议，每次请求之后都会断开链接
用户拿着用户名密码 请求数据 可以返回数据，当请求其他页面时，又要再次输入用户名密码
此时 常见做法 用户请求时会携带自身信息（服务端生成的信息） （Cookie）
Cookie就是用来保存用户身份的信息

"""
