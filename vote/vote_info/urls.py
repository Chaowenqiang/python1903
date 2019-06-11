from django.conf.urls import url
from .views import index,detail,result

app_name = 'vote_info'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^result/(\d+)/$', result, name='result'),
]