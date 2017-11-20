from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^faces/$', views.faces, name='faces'),
    url(r'^account/$', views.account, name='account'),
    url(r'^about/$', views.about, name='about'),
    url(r'^delete\/(?P<picname>.*)/$', views.delete, name='delete'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^pic\/(?P<picname>.*)/$', views.pic, name='pic'),
    url(r'^if_add_face/$', views.if_add_face, name='if_add_face'),
    url(r'^oneface\/(?P<small_pic>.*)/$', views.oneface, name='oneface'),#匹配任意字符串
    url(r'^re_identify/$', views.re_identify, name='re_identify'),
]
