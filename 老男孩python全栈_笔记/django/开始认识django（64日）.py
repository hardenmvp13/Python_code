'''
django框架：
    pip install django
    1，利用命令创建：
        # 创建django程序
        django-admin startproject mysite
        # 进入程序主目录
        cd mysite
        # 启动socket服务端，等待用户发送请求
        python manage.py runserver 127.0.0.1:8080

       也可以pycharm来创建（创建django项目）

    2，django程序目录
        mysite
            mysite
                -setting.py #django配置文件
                -url.py     #路由系统：url——函数的对应关系(函数：处理用户请求并且返回结果)
                -wsgi.py    #用于定义django用什么socket（套接字，网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket），
                             现在用wsgiref（一般用于本地测试，性能比较低  ），以后会用uwsgi

            manage.py #对当前django程序所有操作可以基于python manage.py runserver

django创建步骤
    (1),创建project
    (2),配置
         -模板路径 在project 同级目录创建tamplates文件
            TEMPLATES = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    # 当修改tempalts文件名，这里就会自动修改，BASE_DIR 当前目录路径
                    'DIRS': [os.path.join(BASE_DIR, 'templates')],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.debug',
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ]
         -静态文件路径 在project 同级目录创建static（储存css，js）文件
            # 使用时css，js前的前缀
            STATIC_URL = '/static/'
            # 处理css文件,自动修改文件名
            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, "static"),
            ]
    (3),额外配置  注释掉'django.middleware.csrf.CsrfViewMiddleware',
        MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            # 'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

    （4）url对应关系
        /login/ login
         get请求 ： 只有request.GET
         post请求 ：request.GET 和 request.POST  都可能有值

         def login(request):
            request.method
            request.POST ——》 请求体
            request.GET  ——》  请求头中的url中的值

            return HttpResponse(...) 返回字符串
            return render(request, "login.html", {...})  使用模板
            return redirect("要跳转的网址")

    （5）模板引擎中的特殊标记
        例如：login.html
                {{ name}}

              def login(request):
                return render(request, "login.html", {"name": "alex"})











'''