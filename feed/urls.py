from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # name = URL주소를 ip대신 이름으로 접속 할 수 있게 해준다.
    url(r'^$', views.index, name='index'),
    #주소 뒤에 id값(1,2,3,...)으로 표기된다.
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='index'),
    # url(r'^$', views.about, name='index'),
]
