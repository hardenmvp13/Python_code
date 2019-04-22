'''
64日内容回顾：
    1，web框架本质
        —本质socket
        —http协议
            —模板头
            —模板体
        —模板引擎的渲染是在服务器进行的（本质上传输的是字符串）
    2，django
        — 安装
        — django-admin startproject mysite
        — 配置
            —配置文件
            —静态文件
            —csrf注释
        —urls.py
            url -> 函数
        —函数：
            def index(request):
                request.method
                request.POST
                request.GET

            return HttpResponse(..)
            return render(request, "模板路径", {})
            return redirect("URL")
        —模板渲染
            def index(request):
                return render(request, "模板路径",
                {
                "k1": "v1",
                "k2": [1, 2, 3, 34],
                "k3": {"harden"："mvp"},
                })

            index.html
                <h1>{{ k1 }}</h1>
                <h1>{{ k2.2 }}</h1>
                {% for item in k2%}
                    <h1>{{ item }}</h1>
                {% endfor %}




65日内容：

一，学员管理：
        表：
            班级
            学生

            老师

        单表操作
            增
            删
            改
            查
        一对多操作
            增
            删
            改
            查
        多对多操作
            增
            删
            改
            查
班级表：
id （主键） title
1           一班
2           二班
3           三班

学生表
id（主键）  name  班级id（外键）
1           哈登      1
2           麦迪      2

老师表
id(主键)   name
1           李老师
2           王老师
3           陈老师

老师和班级的关系表：
id      老师id    班级id
1       2           1
2       3           2
3       1           3

django基础：



'''