'''
    创建rss文件及连接
'''
from django.contrib.syndication.views import Feed
from .models import Article


# 死格式
class ArticleFeed(Feed):
    title = 'VenJohn的个人博客'
    description = '关于Django的一些文章'
    link = '/'

    # items不能变，相当于遍历出数据库中的所有书籍
    def items(self, num):
        return Article.objects.all().order_by('-create_time')[:num]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:30]

    def item_link(self, item):
        return '/single/%s'%(item.id,)
