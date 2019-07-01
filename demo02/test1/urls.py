from django.conf.urls import url
from .views import index, list, detail, deletehero, add_hero

# app_name是关键字，不可改，后面的值需要与项目路由include中的namespace一致
app_name = 'test1'

urlpatterns = [
    # url(r'^index/$', index),
    url(r'^$', index, name='index'),
    url(r'^list/$', list, name='list'),
    # 通过正则分组 传递参数 通过（）传参 视图函数需要有形参
    # 第二个参数是调用view.py中的函数，name是对第一个参数重命名
    url(r'^detail/(\d+)/$', detail, name='detail'),

    # 角色删除
    url(r'^deletehero/(\d+)/$', deletehero, name='deletehero'),

    # 添加角色
    url(r'^add_hero/(\d+)/$', add_hero, name='add_hero'),
]
