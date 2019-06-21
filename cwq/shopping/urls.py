from django.conf.urls import url
from . import views
from haystack.views import SearchView

app_name = 'shopping'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list_all/$', views.ListAllView.as_view(), name='list_all'),
    url(r'^crow/(\d+)/$', views.CrowView.as_view(), name='crow'),
    url(r'^style/(\d+)/$', views.StyleView.as_view(), name='style'),
    url(r'^brand/(\d+)/$', views.BrandView.as_view(), name='brand'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', views.LogOutView.as_view(), name='logout'),
    url(r'^active/(.*?)/$', views.ActiveView.as_view(), name='active'),
    url(r'^search/$', SearchView(), name='search'),

]