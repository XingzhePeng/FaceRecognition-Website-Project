from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.activate),
    url(r'^reset/$', views.reset, name='reset'),
    url(r'^reset_au/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.reset_au),
    url(r'^reset_done/$', views.reset_done, name='reset_done'),
    url(r'^sendemail_a/$', views.sendemail_a, name='sendemail_a'),
]
