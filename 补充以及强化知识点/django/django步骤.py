'''
#########################  django  #############################
注意：（1）改过models.py里的东西了，一定要记住重新迁移数据库
      （2）{{ }} 模板变量
          {%  %} 包裹起来的叫做模板标签

  1，搭建开发环境
         1.1 先搭建虚拟环境，用virtualenv +虚拟环境位置（D:\django_blog\django_env）
                    虚拟环境所在地方          C:\Users\Administrator>virtualenv D:\django_blog\django_env
                    激活虚拟环境              C:\Users\Administrator>D:\django_blog\django_env\Scripts>activate
         1.2 新建项目，使用 django-admin startproject +项目名称
                                             (django_env) D:\django_blog\code>django-admin startproject project
         1.3 运行django服务器， python manage.py runserver
                （安装目录依赖 pip install -r requirements.txt）

  2,建立blog应用
         2.1 python manage.py startapp blog      (django_env) D:\django_blog\code\project>python manage.py startapp blog
         （建立好应用后要在settings.py文件里把应用名称放到INSTALLED_APPS 设置项里）

  3,创建django博客的数据库模型（model.py）重点
        3.1 分别创建 文章post ，分类category ，标签tag  数据表  （分别通过 foreinkey， manytomanyfied  外键关联）
                objects = models.Manager()        看情况使用

  4,让django完成翻译：迁移数据库
        4.1 迁移数据库
                python manage.py makemigrations
                python manage.py migrate
        4.2 选择数据库版本（这里选择默认的SQLites）,django已经在settings.py 里为我们做了一些默认的数据库配置

  5,django博客首页视图（这是很入门的写法，Hello World 级别的视图函数）
     写好处理 HTTP 请求(5.1)和返回 HTTP 响应的视图函数(5.2),然后把视图函数绑定到相应的 URL 上(5.3)
    （首先配置 URL，把 URL 和相应的视图函数绑定，一般写在 urls.py 文件里，然后在工程的 urls.py 文件引入）
        5.1 绑定blog\url.py与视图函数blog\view.py
                url(r'^$', views.index, name='index')
                当用户输入网址 http://127.0.0.1:8000 后，Django 首先会把协议 http、域名 127.0.0.1 和端口号 8000 去掉，此时只剩下一个空字符串，
                而 r'^$' 的模式正是匹配一个空字符串（这个正则表达式的意思是以空字符串开头且以空字符串结尾），
                于是二者匹配，Django 便会调用其对应的 views.index 函数。
        5.2 编写视图函数blog\view  这里使用django模板(templates) ---->> Django 要我们把大段的文本写到一个文件里(html)，然后 Django 自己会去读取这个文件，再把读取到的内容传给 HttpResponse
                                首先在project下创建templates\index.html ,
                                        其中{{}}：模板变量 ，Django 在渲染这个模板的时候会根据我们传递给模板的变量替换掉这些变量。最终在模板中显示的将会是我们传递的值。
                                接着在settings.py 找到 TEMPLATES 选项,设置一下模板文件所在的路径
                                          'DIRS': [],
                                           改成：'DIRS': [os.path.join(BASE_DIR, 'templates')],BASE_DIR 是 settings.py 在配置开头前面定义的变量，记录的是工程根目录 blogproject\ 的值，在这个目录下有模板文件所在的目录 templates\，于是利用os.path.join 把这两个路径连起来，构成完整的模板路径
                                最后修改视图函数（view.py）:调用 Django 提供的 render 函数。这个函数根据我们传入的参数来构造 HttpResponse(服务器的响应函数)
        5.3 配置项目project\url.py  (主项目的url)

  6,真正的django博客首页视图（只需专心编写视图函数，让它实现我们想要的功能即可，引入css,js）（重点）
        6.1 首先修改首页的视图函数（把所有文章按最新时间导入进来）(这里objects会出现导入问题，解决在word文档)
        6.2 处理静态文件 （重点，详细看word）（修改css，js成真正的路径）
                {% %} 包裹起来的叫做模板标签，{% load staticfiles %} 这一句一定不要忘记，为了能在模板中使用 {% static %} 模板标签
        6.3 修改静态文件  引入文章，还有post.category.name , post.creates_time  之类的修改

  7,在 Django Admin 后台发布文章
        7.1 创建 Admin 后台管理员账户
                python manage.py createsuperuser
        7.2 在 Admin 后台注册模型(admin.site.register(Post))
        7.3 定制 Admin 后台(希望看到文章的详细信息，比如作者，创建时间，最后修改时间)

  8,博客文章详情页（点进去的文章正文）（detail视图函数）
        有了前面的基础，开发流程都是一样的了：首先配置 URL，即把相关的 URL 和视图函数绑定在一起，然后实现视图函数，编写模板并让视图函数渲染模板。
        8.1 设计文章详情页的URL（blog/urls.py）（当用户访问 <网站域名>/post/1/ 时，显示的是第一篇文章的内容，数字代表了第几篇文章，也就是数据库中 Post 记录的 id 值）
        8.2 编写detail视图函数(记得不要忘记传进来 pk  也就是第几篇文章这个参数)
        8.3 编写详情页模板
                    把 single.html 拷贝到 templates\blog 目录下（和 index.html 在同一级目录），然后改名为 detail.html。
                    在 index 页面博客文章列表的标题和继续阅读按钮写上超链接跳转的链接，即文章 post 对应的详情页的 URL，让用户点击后可以跳转到 detail 页面
        8.4 模板继承

  9，支持 Markdown 语法和代码高亮
        9.1 安装 Python Markdown
                    pip install markdown
        9.2 在 detail 视图中渲染 Markdown
                    对 post 的 body 的值做一下渲染，把 Markdown 文本转为 HTML 文本再传递给模板
                    (但是到这一部，还是不能按照markdown正常显示)
        9.3 safe 标签
                    找到展示博客文章主体的 {{ post.body }} 部分，为其加上 safe 过滤器，{{ post.body|safe }}
        9.4 代码高亮
                    安装 Pygments   pip install Pygments
                    引入样式文件（ .css 样式文件）  有可能会显示错误，问题在于不要复制例子，要从其他地方复制，或者手打上去

  10，页面侧边栏：使用自定义模板标签  （侧边栏有四项内容：最新文章、归档、分类和标签云）
        10.1 模板标签目录结构
                    blog 应用下创建一个 templatetags 文件夹。然后在这个文件夹下创建一个 __init__.py 文件，
                    使这个文件夹成为一个 Python 包，之后在 templatetags\ 目录下创建一个 blog_tags.py 文件
        10.2 编写模板标签代码(每个标签对应一个函数)
                   最新文章模板标签  （类似于 vivews.py 函数里面的 index响应函数）
                   归档模板标签
                   分类模板标签
        10.3 使用自定义的模板标签
                    类似于使用 static 模板标签时曾经导入过 {% load staticfiles %}，这一次在base.html加入{% load blog_tags %}
                    分别在base.html那里修改 最新文章处 ，归档部分 ，分类部分

  11，分类和归档（完善）     完善归档和分类功能，当用户点击归档下的某个日期或者分类下的某个分类时，
                             跳转到文章列表页面，显示该日期或者分类下的全部文章。
        11.1 归档页面
                    在views.py创建archives（归档）函数
                            使用 filter 来根据条件过滤
                            created_time.year，但是由于这里作为函数的参数列表，所以 Django 要求我们把点替换成了两个下划线，即 created_time__year
                    然后配置好URL
                    接着在模板找到归档列表部分的代码，修改超链接的 href 属性，让用户点击超链接后跳转到文章归档页面
                    最后要安装 pytz       pip install pytz
                    重启服务器，就可以了
        11.2 分类页面
                    在views.py创建 categroy（分类）函数
                    配置url
                    修改模板代码（base,html），修改超链接的 href 属性

  12，评论 （重点）comments
        12.1 创建评论应用
                python manage.py startapp comments
        12.2 设计评论的数据库模型
                代码写在 comment\models.py 里,参考blog的数据库建立
        12.3 评论表单设计（表单，新概念，掌握好）
                在comments文件夹下新建 forms.py
        12.4 评论视图函数（重点）
                comments/views.py
        12.5 绑定 URL
                绑定blog\url.py与视图函数blog\view.py
                然后在项目的urls.py 上绑定
        12.6 更新文章详情页面的视图函数
                blog/views.py
        12.7 在前端渲染表单
        12.8 显示评论内容

  13,小问题修正
        13.1 在模型中指定排序
                    各个视图函数中都有类似于 Post.objects.all().order_by('-created_time') 这样的代码，这导致了很多重复。
                    因为只要是返回的文章列表，基本都是逆序排列的，因此我们可以在 Post 模型中指定 Post 的自然排序方式。
                    class Meta:
                        ordering = ['-created_time']
        13.2 完善跳转链接(网页的logo以及首页的跳转)
                    href="{% url 'blog:index' %}"
        13.3 显示正确的评论量
                    {{ post.comment_set.count }}

  14，使用 Nginx 和 Gunicorn 部署 Django 博客
        14.1 部署前的准备
                购买服务器
                购买域名
                搭建服务器
                安装软件
                    在 root 下部署代码不安全，最好是建一个新用户
                       新建用户名                       useradd -m -s /bin/bash 用户名
                       把新创建的用户加入超级权限组     usermod -a -G sudo yangxg
                       为新用户设置密码                 passwd yangxg
                       切换到创建的新用户               su - yangxg
                    新用户创建好以后，最好更新一下系统
                            sudo apt-get update
                            sudo apt-get upgrade
                    接下来就可以安装必要的软件了，这里我们需要用到的软件有 Nginx、Pytohn3、Git、pip 和 virtualenv
                            sudo apt-get install nginx
                            sudo apt-get install git python3 python3-pip
                            sudo pip3 install virtualenv
                    解析域名到服务器的 IP 地址
                    启动 Nginx 服务

        14.2 部署代码
                部署前的项目配置
                将代码上传到 GitHub
                设置服务器目录结构
                安装项目依赖
                收集静态文件
                生成数据库
                创建超级用户
                配置 Nginx
                使用 Gunicorn
                自动启动 Gunicorn
                使用 CDN 加快 Bootstrap 和 jQuery 的加载速度

  15，使用 Fabric 自动化部署（还未实践）

  16，统计文章阅读量    文章每被浏览一次，则其阅读量 +1，即所谓的文章页面 PV（Page View）数
        16.1 增加新字段
                在blog/models.py  添加views = models.PositiveIntegerField(default=0)
        16.2 增加模型方法
                在blog/models.py下：
                    def increase_views(self):
                        self.views += 1
                        self.save(update_fields=['views'])
        16.3 迁移数据库
        16.4 修改视图函数
                    在blog/views.py下 添加 post.increase_views()
        16.5 在模板中显示阅读量
                添加{{ post.views}}进 details.html 和 index.html

  17，自动生成文章摘要   只要摘取正文的前 N 个字符作为摘要，以便提供文章预览就可以了。因此我们来实现如果文章没有输入摘要，则自动摘取正文的前 N 个字符作为摘要，
        17.1 在blog/models.py下   写一个save()函数，从而保存文章[:n]个字符





'''








