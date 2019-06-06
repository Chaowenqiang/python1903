from django.conf.urls import url
from .views import index,list,detail

app_name = 'test1'

urlpatterns = [
    # url(r'^index/$', index),
    url(r'^$', index,name='index'),
    url(r'^list/$', list,name='list'),
    # 通过正则分组 传递参数 通过（）传参 视图函数需要有形参
    url(r'^detail/(\d+)/$', detail,name='detail'),
]