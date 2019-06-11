from django.shortcuts import render,redirect,reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .models import *


# Create your views here.

def checklogin(func):
    def check(self, req, *args):
        if req.COOKIES.get('username'):
            return func(self, req, *args)
        else:
            return redirect(reverse('vote_info:login'))
            # return HttpResponse('qqq')
    return check


class IndexView(View):
    '''
    通过重写父类View方法实现完成通用视图类的功能
    重写get方法代表重写get请求
    '''
    @checklogin
    def get(self, req):
        questions = Questions.objects.all()

        # 这里locals()等同于{'question':question}
        return render(req, 'index.html', locals())


class DetailView(View):

    @checklogin
    def get(self, req, id):
        questions = Questions.objects.get(pk=id)
        return render(req, 'detail.html', locals())

    @checklogin
    def post(self, req, id):
        c_id = req.POST.get('votes')
        choice = Votes.objects.get(pk=c_id)
        choice.votes += 1
        choice.save()
        return redirect(reverse('vote_info:result', args=(id,)))


class ResultView(View):

    @checklogin
    def get(self, req, id):
        questions = Questions.objects.get(pk=id)
        return render(req, 'result.html', locals())


class LoginView(View):

    def get(self, req):
        return render(req, 'login.html')

    def post(self, req):
        username = req.POST.get('username')
        pwd = req.POST.get('possword')
        # 查询数据库是否存在该用户，如果有则登陆成功，跳转到首页  需要设置cookie
        # cookie是在response里设置
        res = redirect(reverse('vote_info:index'))
        res.set_cookie('username', username)
        return res



# def index(req):
#     questions = Questions.objects.all()
#     print(questions)
#
#     return render(req, 'index.html', {'questions': questions})
#
#
# def detail(req, id):
#     questions = Questions.objects.get(pk=id)
#     if req.method == 'GET':
#
#         return render(req, 'detail.html', {'questions': questions})
#     elif req.method == 'POST':
#
#         c_id = req.POST.get('votes')
#         c = Votes.objects.get(pk=c_id)
#         c.votes += 1
#         c.save()
#
#         # post请求之后必须用重定向，不能用render，因为render只起渲染界面的作用
#         return HttpResponseRedirect('/result/%s/' % (id,))
#         return HttpResponseRedirect('vote_info:result', arges=(id,))
#
#
#
# def result(req, id):
#     question = Questions.objects.get(pk=id)
#     return render(req, 'result.html', {'question': question})
