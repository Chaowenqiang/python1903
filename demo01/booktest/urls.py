from django.conf.urls import url
from .views import index,list,detail

urlpatterns = [
    url(r'^index/$', index),
    url(r'^list/$', list),
    # 通过正则分组 传递参数 通过（）传参 视图函数需要有形参
    url(r'^detail/(\d+)/$', detail),
]