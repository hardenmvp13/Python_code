from django.conf.urls import url
from . import views

'''
url(r"^$",views.index,name="index")
     本地开发服务器的域名是 http://127.0.0.1:8000，那么当用户输入网址 http://127.0.0.1:8000 后，Django 首先会把协议 http、域名 127.0.0.1 和端口号 8000 去掉，
     此时只剩下一个空字符串，而 r'^$' 的模式正是匹配一个空字符串（这个正则表达式的意思是以空字符串开头且以空字符串结尾），
     于是二者匹配，Django 便会调用其对应的 views.index 函数
 '''
app_name = "blog"
urlpatterns = [
    url(r"^$",views.index,name="index"),      #首页请求函数(index)
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name="detail"),  #文章详情页函数(detail)
]