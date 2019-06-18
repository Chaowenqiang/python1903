from django.conf.urls import url
from . import views
from .feed import ArticleFeed
from haystack.views import SearchView

app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index_view, name='index'),
    url(r'^single/(\d+)/$', views.SingleView.as_view(), name='single'),
    url(r'^archive/(\d+)/(\d+)/$', views.ArchiveView.as_view(), name='archive'),
    url(r'^category/(\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(\d+)/$', views.TagView.as_view(), name='tag'),
    url(r'^rss/$', ArticleFeed(), name='rss'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^search/$', SearchView(), name='search'),
]