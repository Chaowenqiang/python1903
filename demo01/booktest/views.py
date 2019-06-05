from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book_info,Hero_info

# Create your views here.


def index(req):


    # 1获取模板
    temp = loader.get_template('booktest/index.html')
    # 2使用模板动态渲染数据
    res = temp.render({})
    # 3返回渲染结果
    return HttpResponse(res)
    # return HttpResponse('这是index界面')

def list(req):

    books = Book_info.objects.all()

    temp = loader.get_template('booktest/list.html')
    res = temp.render({'books':books})
    return HttpResponse(res)
    # return HttpResponse('这是列表页面')

def detail(req, id):

    book = Book_info.objects.get(pk=id)

    temp = loader.get_template('booktest/detail.html')
    res = temp.render({'book':book})
    return HttpResponse(res)
    # return HttpResponse('这是详情页%s'%(id,))
