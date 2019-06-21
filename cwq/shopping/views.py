from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views import View
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from itsdangerous import TimedJSONWebSignatureSerializer
from django.contrib.auth import authenticate,login,logout
from haystack.views import SearchView

# Create your views here.


# 定义分页函数
def get_page_info(req, queryset, per_page, path):
    paginator = Paginator(queryset, per_page)
    page_num = req.GET.get('page')
    page_num = 1 if page_num == None else page_num
    page = paginator.get_page(page_num)
    page.path = path
    return page


# 创建首页视图
class IndexView(View):

    def get(self, req):
        goodses = GoodsInfo.objects.all()
        path = '/'
        page = get_page_info(req, goodses, 4, path)
        return render(req, 'shopping/index.html', locals())


# 全商品界面
class ListAllView(View):

    def get(self, req):
        goodses = GoodsInfo.objects.all()
        path = '/list_all/'
        page = get_page_info(req, goodses, 1, path)
        return render(req, 'shopping/list.html', {'page':page})


# 创建适宜人群视图
class CrowView(View):

    def get(self, req, id):
        crow = get_object_or_404(Crow, pk=id)
        goodses = crow.goodsinfo_set.all()
        path = '/crow/%s/'%(id,)
        page = get_page_info(req, goodses, 1, path)
        return render(req, 'shoppng/list.html', {'page':page})


# 创建款式视图
class StyleView(View):

    def get(self, req, id):
        style = get_object_or_404(Style, pk=id)
        goodses = style.goodsinfo_set.all()
        path = '/style/%s/'%(id,)
        page = get_page_info(req, goodses, 1, path)
        return render(req, 'shopping/list.html', {'page':page})


# 创建品牌视图
class BrandView(View):

    def get(self, req, id):
        brand = get_object_or_404(Brand, pk=id)
        goodses = brand.goodsinfo_set.all()
        path = '/brand/%s'%(id,)
        page = get_page_info(req, goodses, 1, path)
        return render(req, 'shopping/list.html', {'page': page})


# 创建联系我们视图
class ContactView(View):

    def get(self, req):
        return render(req, 'shopping/contact.html')

    def post(self, req):

        contact = Contact()
        name = req.POST.get('name')
        email = req.POST.get('email')
        content = req.POST.get('content')
        contact.name = name
        contact.email = email
        contact.content = content
        contact.save()
        return redirect(reverse('shopping:index'))


# 登录
class LoginView(View):

    def get(self, req):
        return render(req, 'shopping/login.html')

    def post(self, req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        # 从数据库获取用户信息
        user = UserInfo.objects.filter(username=username).first()
        # 判断用户是否存在
        if user:
            # 判断密码
            if user.check_password(password):
                # 判断用户是否激活
                if user.is_active:
                    # authenticate可以判断session,cookie等信息，然后进行授权
                    user1 = authenticate(req, username=username, password=password)
                    # 在浏览器中存储cookie值
                    login(req, user1)
                    return redirect(reverse('shopping:index'))
                else:
                    error_message = '账户未激活'
                    return render(req, 'shopping/login.html', locals())
            else:
                error_message = '密码错误'
                return render(req, 'shopping/login.html', locals())
        else:
            error_message = '账户不存在'
            return render(req, 'shopping/login.html', locals())



# 注册
class RegisterView(View):

    def get(self,req):

        return render(req, 'shopping/register.html')

    def post(self, req):

        try:
            username = req.POST.get('username')
            password = req.POST.get('password')
            email = req.POST.get('email')
            # 向数据库写入数据并判断是否重复
            user = UserInfo.objects.create_user(username=username, password=password, email=email)
            # 将数据库中的is_active改为False
            user.is_active = False
            user.save()

            # 向用户邮箱发送邮件
            from django.core.mail import EmailMultiAlternatives
            from django.conf import settings
            # 获取用户的id，用于激活邮件时使用
            user_id = user.id
            # 获取密钥加密
            util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY,)
            # 对用户的id反序列化并进行解密
            user_id = util.dumps({'user_id':user_id}).decode('utf-8')

            # 创建邮件信息，包括邮件标题，邮件内容，发送者，接收者
            info = '<h1><a href="http://127.0.0.1:8000/active/%s/">点击激活账户%s</a></h1>' % (user_id, username)
            mail = EmailMultiAlternatives(subject= '激活邮件',
                                          body= info,
                                          from_email= settings.DEFAULT_FROM_EMAIL,
                                          to= [email])
            # 设置文本格式
            mail.content_subtype = 'html'
            # 发送邮件
            mail.send()

            # 判断用户是否写入成功
            if user:
                return redirect(reverse('shopping:login'))
        except:
            error_message = '账户名已存在，请重新注册'
            return render(req, 'shopping/register.html', locals())


class LogOutView(View):

    def get(self, req):
        logout(req)
        return redirect(reverse('shopping:index'), locals())


# 创建激活视图
class ActiveView(View):

    # 此处req不可删除
    def get(self, req, id):

        from django.conf import settings
        util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY, )
        obj = util.loads(id)
        # 此处user_id需要与上边dump中传的键相同
        id = obj['user_id']
        user = UserInfo.objects.get(pk=id)
        if user:
            user.is_active = True
            user.save()
            return redirect(reverse('shopping:login'))


# class Search_View(SearchView):
#
#     def get(self, req):


