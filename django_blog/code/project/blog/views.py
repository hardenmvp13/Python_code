#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
'''
render()函数，在django.shortcuts包里
render（request，template_name，context = None，content_type = None，status = None，using = None）
必需参数
    request  用于生成此响应的请求对象。
    template_name  要使用的模板的全名或模板名称的序列。如果给出了序列，则将使用存在的第一个模板。
可选参数¶
    context       要添加到模板上下文的值的字典。默认情况下，这是一个空字典。如果字典中的值是可调用的，则视图将在呈现模板之前调用它。
    content_type  用于生成的文档的MIME类型。默认为DEFAULT_CONTENT_TYPE设置的值。
    status        响应的状态代码。默认为200。
    using         该NAME模板引擎的使用加载的模板。
'''
#首页函数响应函数，helloword级别
# def index(request):
#     '''return HttpResponse("你好，加油学python啊，好好努力")'''
#     return render(request,template_name="blog/index.html",context={
#         "title":"我要好好学习编程",
#         "welcome":"欢迎来学python",
#         "harden":"好好学习，好好锻炼身体"
#     })


'''
post_list = Post.objects.all().order_by("-created_time")
return render(request,template_name="blog/index.html",context={
    "post_list": post_list,
})
    模型管理器 objects 的使用。这里我们使用 all() 方法从数据库里获取了全部的文章，存在了 post_list 变量里。
    all 方法返回的是一个 QuerySet（可以理解成一个类似于列表的数据结构），由于通常来说博客文章列表是按文章发表时间倒序排列的，
    即最新的文章排在最前面，所以我们紧接着调用了 order_by 方法对这个返回的 queryset 进行排序。
    排序依据的字段是 created_time，即文章的创建时间。- 号表示逆序，如果不加 - 则是正序。
    接着如之前所做，我们渲染了 blog\index.html 模板文件，并且把包含文章列表数据的 post_list 变量传给了模板。
 '''
#真正的首页响应函数（index）
def index(request):
    #all() 方法从数据库里获取了全部的文章，存在了 post_list 变量里。
    post_list = Post.objects.all().order_by("-created_time")
    return render(request,template_name="blog/index.html",context={
        "post_list": post_list,
    })
import markdown
from django.shortcuts import get_object_or_404
#首页详情页函数（detail）
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)

    #extra 本身包含很多拓展，而 codehilite 是语法高亮拓展，这为我们后面的实现代码高亮功能提供基础，
    #而 toc 则允许我们自动生成目录
    post.body = markdown.markdown(post.body,
                                  extensions = [
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    return render(request,template_name="blog/detail.html",context={
        "post":post
    })



