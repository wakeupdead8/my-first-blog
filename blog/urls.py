from django.conf.urls import  include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^post/$', views.post, name='post'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]