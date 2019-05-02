'''
介绍 ： django项目开发必须懂的知识点，下面使用的数据库是mysql ,

models.py  数据库表结构，

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Test(models.Model):

    name = models.CharField(max_length=20)


1、GET 请求：

urls.py

"""pythondjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from BlogDjango import views
from polls import views as pollsviews, search, search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/+\d', views.hello),
    url(r'^base/', views.base),
    url(r'^testdb$', pollsviews.testdb),
    url(r'^querydb$', pollsviews.selectDB),
    url(r'^updateDB$', pollsviews.updateDB),
    url(r'^deleteDB$', pollsviews.deleteDB),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]


新建一个search.py

# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    return render_to_response('search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    print request.GET
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

创建一个页面

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search" method="get">
        <input type="text" name="q">
        <input type="submit" value="搜索">
    </form>
</body>
</html>

结果：
1、


   2、







2、POST请求（重要）

注意：请求之后，经过我们自己的逻辑处理后，如何返回到页面并且解析：

新建一个search2.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {'rlt': 10000}
    print request.POST
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

urls.py

"""pythondjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from BlogDjango import views
from polls import views as pollsviews, search, search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/+\d', views.hello),
    url(r'^base/', views.base),
    url(r'^testdb$', pollsviews.testdb),
    url(r'^querydb$', pollsviews.selectDB),
    url(r'^updateDB$', pollsviews.updateDB),
    url(r'^deleteDB$', pollsviews.deleteDB),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]

post.html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search-post" method="post">
        {% csrf_token %}
        <input type="text" name="q">
        <input type="submit" value="Submit">
    </form>

    <p>{{ rlt }}</p>
</body>
</html>
结果：





注意：
     在模板的末尾，我们增加一个 rlt 记号，为表格处理结果预留位置。

     表格后面还有一个{% csrf_token %}的标签。csrf 全称是 Cross Site Request Forgery。这是Django提供的防止伪装提交请求的功能。POST 方法提交的表格，必须有此标签。


'''
'''
POST和GET差异：

1. POST和GET是HTTP协议定义的与服务器交互的方法。GET一般用于获取/查询资源信息，而POST一般用于更新资源信息。另外，还有PUT和DELETE方法。

2. POST和GET都可以与服务器完成查，改，增，删操作。

3. GET提交，请求的数据会附在URL之后，以？分割URL和传输数据，多个参数用&连接；

    POST提交，把提交的数据放置在HTTP包的包体中；因此，GET提交的数据会在地址栏中显示出来，而POST提交，地址栏不会改变。

    HTTP协议没有对传输的数据大小进行限制，HTTP协议规范也没有对URL长度进行限制。

但是，特定浏览器和服务器对URL长度有限制，如IE对URL长度的限制是2083字节。因此，GET提交时，传输数据就会受到URL长度的限制。

4. 对于GET方式，服务器端用Request.QueryString获取变量的值，对于POST方式，服务器端用Request.Form获取提交的数据。

判断法方法： if request.method == 'GET':'''