from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView
from .models import Article, Tag, Category,MessageInfo
from comments.forms import CommentForm
from django.core.paginator import Paginator
from django.http import HttpRequest
import markdown


# Create your views here.


def get_page_info(request, queryset, path, per_page=1):

    # 分页操作，每页显示几个
    paginator = Paginator(queryset, per_page)
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum == None else pagenum
    page = paginator.get_page(pagenum)
    page.path = path
    return page


class AboutView(View):

    def get(self, req):
        return render(req, 'blog/about.html')


class IndexView(View):

    def get(self, req):
        # 从数据库中查询所有的文章
        articles = Article.objects.all()

        page = get_page_info(req, articles, '/')

        # 渲染指定的html页面，locals()等同于{'articles':articles}用于向前端页面传输数据，且前端接收数据的字段应与字典中的键相同
        return render(req, 'blog/index.html', {'page': page})


class SingleView(View):

    def get(self, req, id):
        # get_object_or_404方法可以从指定的数据库中得到指定的数据，没有则返回404
        article = get_object_or_404(Article, pk=id)

        # 1、获取markdown实例
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        # 2、使用makedown实例渲染指定字段
        article.body = md.convert(article.body)
        # 3、将md的目录对象赋值给article
        article.toc = md.toc

        # 向页面传递一个评论表单
        cf = CommentForm()

        return render(req, 'blog/single.html', locals())

    def post(self, req, id):
        # 实例化模型，req.POST用于接收前端页面返回的数据
        cf = CommentForm(req.POST)
        # 如果表单数据有效
        if cf.is_valid():
            # 通过cf的save方法得到模型类（Comment的实例）
            c = cf.save(commit=False)
            c.article = get_object_or_404(Article, pk=id)
            # 保存数据
            c.save()
            # 重定向到指定路由
            return redirect(reverse('blog:single', args=(id,)))


# 创建时间归类函数
class ArchiveView(View):

    def get(self, req, year, month):

        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
        page = get_page_info(req, articles, '/archive/%s/%s/' % (year, month), 2)

        return render(req, 'blog/index.html', {'page': page})


class CategoryView(View):

    def get(self, req, id):

        category = get_object_or_404(Category, pk=id)
        articles = category.article_set.all()
        page = get_page_info(req, articles, '/category/%s/' % (id,), 2)

        return render(req, 'blog/index.html', {'page': page})


class TagView(View):

    def get(self, req, id):

        tag = get_object_or_404(Tag, pk=id)
        articles = tag.article_set.all()
        page = get_page_info(req, articles, '/tag/%s/' % (id,))

        return render(req, 'blog/index.html', {'page': page})


class ContactView(View):

    def get(self, req):

        return render(req, 'blog/contact.html')

    def post(self, req):
        mi = MessageInfo()
        mi.name = req.POST.get('name')
        mi.email = req.POST.get('email')
        mi.content = req.POST.get('message')
        mi.save()
        return redirect(reverse('blog:contact'))


