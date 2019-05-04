'''
使用环境：Windows+python3.4+MySQL5.5+Navicat

一、创建连接

1.准备工作，想要使用Python操作MySQL，首先需要安装MySQL-Python的包，在Python 3.x下，该包已经改名为MySQLClient。可以使用pip方式安装：

pip install MySQLClient


或者下载包文件，进行安装也可以。

2.Python使用MySQL的流程：



3.启动MySQL服务器：以管理员身份启动“cmd”，输入命令：’net start mysql‘

Python中使用MySQL导入方法：import MySQLdb

4.创建Connection

　　Connection：创建了Python客户端与数据库之间的网络通路。他的参数如下

参数名	类型	说明
host	String	MySQL的服务器地址
port	int	    MySQL的端口号
user	String	用户名
passwd	String	密码
db	    String	使用的数据库
charset	String	连接字符集
Connection支持的方法：
方法名	说明
cursor（）	创建并且返回游标
commit（）	提交当前事物
rollback()	回滚当前事物r()
close()	关闭Connection
5.获取Cursor.

Cursor:游标对象，用于执行查询和获取结果，它支持的方法如下：

方法名	说明
execute()	用于执行一个数据库的查询命令
fetchone()	获取结果集中的下一行
fetchmany(size)

获取结果集中的下（size）行
fetchall()	获取结果集中剩下的所有行
rowcount	最近一次execute返回数据/影响的行数
close()	关闭游标
下面我们在Python中创建一个实例：

复制代码
import MySQLdb

conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='199331',db='test',charset='utf8')

cursor=conn.cursor()

print(conn)
print(cursor)

cursor.close()
conn.close()
复制代码
运行程序结果如下：

从结果中我们可以看见成功创建了一个Connection和Cursor对象。

二、建立数据库，进行一些简单操作

1.简单的创建一个’user‘表，并且插入一些数据。user表中只有两个字段：userid和username。代码如下：

复制代码
import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='199331',db='test',charset='utf8')
cur=conn.cursor()

cur.execute("""
create table if not EXISTS user
(
  userid int(11) PRIMARY KEY ,
  username VARCHAR(20)
)
""")
for i in range(1,10):
    cur.execute("insert into user(userid,username) values('%d','%s')" %(int(i),'name'+str(i)))
conn.commit()

cur.close()
conn.close()
复制代码
我们用Navicat打开数据库，查看一下结果，，可以看到成功创建表，并且插入了十个数据。

2.我们操作一下Cursor里面的一些方法。

　　execute()方法：执行SQL，将一个结果从数据库获取到客户端

　　fetch*（）方法：移动rownumber，返回数据。

例如我们有如下代码：

1
2
3
4
5
6
7
8
9
10
sql='select * from user'
cursor.execute(sql)

print(cursor.rowcount)

rs=cursor.fetchone()
print(rs)

rs=cursor.fetchmany(3)
print(rs)
rs=cursor.fetchall()print(rs)
 结果如下：



我们可以看出执行查询全部数据后，rowcount为10

执行fetchone（）方法后返回一个数据，执行fetchmany(3)后返回3条数据，执行fetchall（）后返回剩下的所有数据。

再有如下代码：

1
2
3
res=cursor.fetchall()
for row in res:
    print('userid=%s,userna=%s' %row)
 此时的执行结果为：



3.上面介绍的便是数据库中常说的Select操作，下面我们介绍数据的更新，即：insert、update、delete操作。值得注意的是在这部分操作时需要注意的是是否数据发生异常，如果数据没有发生异常，我们便可以直接使用commit()进行提交（注：如没有使用commit，则数据库不会发生任何变化）。但是如果出现了异常，那么久需要使用rollback()进行回滚。

3.1先来看一个没有异常，正常提交的例子：

1
2
3
4
5
6
7
8
9
10
sql_insert='insert into user(userid,username) values(10,"name10")'
sql_update='update user set username="name91" where userid=9'
sql_delete='delete from user where userid=3'

cursor.execute(sql_insert)
print(cursor.rowcount)
cursor.execute(sql_update)
print(cursor.rowcount)
cursor.execute(sql_delete)
print(cursor.rowcount)
conn.commit()
 上面的操作即是：添加一条（10，’name10‘）的数据、将userid=9的username修改为’name91‘，删除userid=3的数据，执行上面代码后我们来用Navicat查看一下数据：

从结果可以看到代码执行正常。

3.2.再来看一个有异常的数据

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
sql_insert='insert into user(userid,username) values(10,"name10")'
sql_update='update user set username="name91" where userid=9'
# sql_delete='delete from user where userid=3'
# ##error
sql_delete='delete from user where useri=3'
try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
except Exception as e:
    print(e)
    conn.rollback()
 这里的insert和update操作一样，只不过把delete里面的userid字段错误的写成了useri，执行代码：



可以看到显示出异常，这时我们来看一下数据库数据：

数据没有任何改变。这就是rollback（）的作用

因此，我们以后再写增删改查操作时，最好把操作放入一个try控制块中，来避免一些不必要的错误。

下面是一个银行转账的实例：

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
#-*-encoding:utf-8 -*-

import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='199331',db='test',charset='utf8')
cur=conn.cursor()
##创建数据表
cur.execute("""
create table if not EXISTS account(
  accid int(10) PRIMARY KEY ,
  money int(10)
)
""")
###插入两行数据
cur.execute('insert into account(accid,money) VALUES (1,110)')
cur.execute('insert into account(accid,money) VALUES (2,10)')
conn.commit()

cur.close()
conn.close()


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
#-*- encoding:utf-8 -*-
import sys
import MySQLdb

class TransferMoney(object):
    def __init__(self,conn):
        self.conn=conn
    def check_acct_available(self,accid):
        cursor=self.conn.cursor()
        try:
            sql='select * from account where accid=%s' %accid
            cursor.execute(sql)
            print('check_acct_available'+sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception('账号%s 不存在' %accid)
        finally:
            cursor.close()
    def has_enough_money(self,accid,money):
        cursor=self.conn.cursor()
        try:
            sql='select * from account where accid=%s and money>%s' %(accid,money)
            cursor.execute(sql)
            print('check_money_available'+sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception('账号%s 没有足够钱' %accid)
        finally:
            cursor.close()
    def reduce_money(self,accid,money):
        cursor=self.conn.cursor()
        try:
            sql='update account set money=money-%s where accid=%s' %(money,accid)
            cursor.execute(sql)
            print('reduce money'+sql)
            rs=cursor.fetchall()
            if cursor.rowcount!=1:
                raise Exception('账号%s 减款失败' %accid)
        finally:
            cursor.close()
    def add_money(self,accid,money):
        cursor=self.conn.cursor()
        try:
            sql='update account set money=money+%s where accid=%s' %(money,accid)
            cursor.execute(sql)
            print('reduce money'+sql)
            rs=cursor.fetchall()
            if cursor.rowcount!=1:
                raise Exception('账号%s 加款失败' %accid)
        finally:
            cursor.close()
    def transfer(self,source_accid,target_accid,money):
        ###检测两个账号是否可用
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            ####检测付款人是否有足够的钱
            self.has_enough_money(source_accid,money)
            self.reduce_money(source_accid,money)
            self.add_money(target_accid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e



if __name__=='__main__':
    source_accid=sys.argv[1]
    target_accid=sys.argv[2]
    money=sys.argv[3]

    conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='199331',db='test',charset='utf8')
    tr_money=TransferMoney(conn)

    try:
        tr_money.transfer(source_accid,target_accid,money)
    except Exception as e:
        print('出现问题'+str(e))
    finally:
        conn.close()
'''