"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
#from django.conf.urls import url
from django.conf.urls import url,include
from django.contrib import admin

'''
url(r"",include("blog.urls")),导入了一个 include 函数，把 blog 应用下的 urls.py 文件包含了进来
                              r''，这是一个空字符串,Django 会把这个字符串和后面 include 的 urls.py 文件中的 URL 拼接
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"",include("blog.urls")),
]
