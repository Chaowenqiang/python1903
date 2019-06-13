from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View,ListView
from .models import Article,Tag,Category
from comments.forms import CommentForm
# Create your views here.


class IndexView(View):

    def get(self, req):
        # 从数据库中查询所有的文章
        articles = Article.objects.all()
        # 渲染指定的html页面，locals()等同于{'articles':articles}用于向前端页面传输数据，且前端接收数据的字段应与字典中的键相同
        return render(req, 'blog/index.html', locals())


class SingleView(View):

    def get(self, req, id):

        # get_object_or_404方法可以从指定的数据库中得到指定的数据，没有则返回404
        article = get_object_or_404(Article, pk=id)
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

