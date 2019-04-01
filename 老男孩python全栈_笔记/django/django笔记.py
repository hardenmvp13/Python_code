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

       也可以pycharm来创建：

    2，django程序目录
        mysite
            mysite
                -setting.py #django配置文件
                -url.py     #路由系统：url——函数的对应关系(函数：处理用户请求并且返回结果)
                -wsgi.py    #用于定义django用什么socket（套接字，网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket），
                             现在用wsgiref（一般用于本地测试，性能比较低  ），以后会用uwsgi

            manage.py #对当前django程序所有操作可以基于python manage.py runserver

'''