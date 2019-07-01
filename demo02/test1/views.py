from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookInfo, HeroInfo
from django.template import loader


# Create your views here.


def index(req):
    # # 1获取模板
    # temp = loader.get_template('test1/index.html')
    # # 2使用模板动态渲染数据
    # res = temp.render({})
    # # 3返回渲染结果
    # return HttpResponse(res)

    return render(req, 'test1/index.html')


def list(req):
    books = BookInfo.objects.all()

    # temp = loader.get_template('test1/list.html')
    # res = temp.render({'books':books})
    # return HttpResponse(res)

    return render(req, 'test1/list.html', {'books': books})


def detail(req, id):
    book = BookInfo.objects.get(pk=id)

    # temp = loader.get_template('test1/detail.html')
    # res = temp.render({'book':book})
    # return HttpResponse(res)

    return render(req, 'test1/detail.html', {'book': book})


def deletehero(req, id):
    hero = HeroInfo.objects.get(pk=id)
    hero.delete()
    return HttpResponseRedirect('/detail/%s/' % (hero.book.id), )
    # return HttpResponse('删除%s'%(id,))


def add_hero(req, id):

    book = BookInfo.objects.get(pk=id)
    if req.method == 'GET':
        print('=====================================')
        print(type(req))
        print('=====================================')
        return render(req, 'test1/add_hero.html', {'book': book})
    elif req.method == 'POST':
        hero = HeroInfo()
        hero.name = req.POST.get('heroname')
        hero.content = req.POST.get('herocontent')
        hero.book = book
        hero.save()
        return HttpResponseRedirect('/detail/%s/' % (id,))

# def addhero(req,id):
#     book = BookInfo.objects.get(pk=id)
#     # return HttpResponse("添加成功%s"%(id,))
#     if req.method == "GET":
#         return render(req,"booktest/addhero.html",{"book":book})
#     elif req.method == "POST":
#         hero = HeroInfo()
#         hero.name = req.POST.get("heroname")
#         hero.content = req.POST.get("herocontent")
#         hero.book = book
#         hero.save()
#         return HttpResponseRedirect("/detail/%s/"%(id,))
