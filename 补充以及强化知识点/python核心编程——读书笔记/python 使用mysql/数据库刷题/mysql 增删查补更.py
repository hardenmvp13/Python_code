'''
MySQL：众多关系型数据库中的一种
仓库 --数据库
箱子 --表
数据库：
进入mysql 命令行: mysql -uroot -p
查看所有数据库: show databases;
创建数据库： create database niu charset utf8;
删除数据库： drop database niu;
选择数据库： use databases;
查看所有表： show tables;
查看创建数据库的语句：show create database databasename;
查看创建表的语句：show create table tablename;
查看表结构：desc tablenmae;
'''


'''
                       表：
约束
#自增长       auto_increment
#非空         not null
#默认值       default 'xx'
#唯一         unique
#指定字符集   charset
#主键         primary key
#外键         增加两个表之间的联系(比如两个表都有学生的名字)

#########增##########：
#学生表
create table students(
id int auto_increment primary key，
name varchar(10) not null，
sex varchar(3) default '女',
address varchar(50),
phone int not null unique,
age，
);
#成绩表
create table scores(
id int auto_increnent primary key,
s_id int not null,
grade float not null,
);

###########删############:
drop table tablename;
truncate tablename;#快速删除表

###########改############:
alter table oldtable rename newtable; #改表名
alter table tablename modify name varchar(20);#改表结构
alter table tablename change name newname varchar(20);#改表结构
alter table tablename add age float after name;#新增字段的位置

###########查############：
show create table tablename ;#查看新建表语句
desc table;#查看表结构
show tables ;#查看所有表

'''
'''
                          数据：
########增########
insert into student (name,money,sex,phone) values ('hk',10000,'男',188);
insert into student values('','小明',100,'',120);
########删#########
turncate tablename； #删除整表数据，自增长id从头再来，快速，从磁盘直接删除，不可恢复
delete from student；
#删除整个表的数据，自增长继续
##########改#######
update student set money=100；#不指定条件，修改所有
update student set money=110 where name='hk';#只改hk
自动提交
取消自动提交   set @@autocommitt=0;
                select @@autocommitt=0;
#自动提交取消后，当前会话显示已经成功执行，其实后台并没有执行

############查#########：
select * from students limit 1,5; #从第几条开始，下面的x条，不包含开始的那一条
SELECT * from students limit 5;查询5条
SELECT id,stu_name,sex,money,phone from students;#指定查询的字段
SELECT * from students;#查询所有的数据
SELECT * from students where sex='男';#指定条件
SELECT * from students where sex='男' and money>100; #多个条件，必须同时满足
SELECT * from students where sex='男' or sex='未知' ; #多个条件，有一个满足即可
SELECT * from students where sex !='男'; #<>也是不等于
SELECT * FROM students where addr like '%东京%';#模糊匹配，%代表的是通配符，必须得用like
SELECT * from students a where a.stu_name like '姚_';#_通配符表示任意一个单字符，姚字后面只能跟一个字
SELECT a.stu_name '学生名称',a.phone '学生电话' from students as a where a.stu_name='姚远';#给表起别名,as可以省略
SELECT * from students a where a.stu_name in ('牛牛','林倩','林远');# in
SELECT * from students a where a.money BETWEEN 1000 and 10000;#在什么什么之间的数据
SELECT * from students ORDER BY money desc;
#order by xxx desc，根据哪个字段继续排序，默认是升序，
降序是desc，升序asc
SELECT * from students a where a.addr = '' or a.addr is null; #查询字段为空的数据
SELECT DISTINCT a.money from students a ;#去重
SELECT COUNT(*) '学生人数' from students where sex='女'; #统计行数
SELECT MAX(a.money) 钱最多 from students a; #最大值
SELECT min(money) 钱最少 from students;#最小值
SELECT AVG(a.money) 平均多少钱 from students a; #平均数
SELECT sum(a.money) 总共多少钱 from students a;#总和
SELECT sex 性别,count(*) 人数 from students GROUP BY sex; #分组
SELECT
sex 性别,
count(*) 人数,
a.stu_name 名字

FROM
students a  WHERE a.money > 300 GROUP BY a.id HAVING a.stu_name LIKE '姚%';
#如果group by后面有条件的话，必须得用having子句，having子句里面用到的字段必须出现在select后面，如果group by和order by一起用的话，order by必须写在group by后面
SELECT *,COUNT(*) from students GROUP BY sex,class; #多个字段进行分组

SELECT id,stu_name from students UNION SELECT id,t_name from teacher;
#用来合并两条select语句的结果，两条select语句字段数量要一致，并且数据类型也要一致
union和union all的区别就是一个会去重一个不会

多表关联：
SELECT * FROM USER a, accounts b WHERE
a.id = b.user_id
AND a.username = 'niuhy';
-- SELECT * from students a ,scores b where a.id=b.s_id; -- 多表关联
-- 两个表里面都存在的数据查出来
SELECT * from students a LEFT JOIN scores b on a.id=b.s_id;
-- LEFT JOIN会把左边表所有的数据都查出来，右边表有匹配的就查出来
SELECT * from students a RIGHT JOIN scores b on a.id=b.s_id;
-- RIGHT JOIN会把右边表所有的数据都查出来，左边表有匹配的就查出来
SELECT * from students a inner JOIN scores b on a.id=b.s_id;
-- INNER JOIN两边表里都匹配的数据才查到
子查询：
把一条sql的结果，作为另一条sql的条件
SELECT * from scores a where a.s_id = (SELECT id from students where stu_name='牛牛');

把子查询当成一个表
SELECT
a.grade 成绩,
b.stu_name 学生名称,
b.id 学号
FROM
scores a,
( SELECT id,stu_name FROM students WHERE stu_name = '牛牛') b
WHERE
a.s_id = b.id;
数据库权限：
mysql数据的权限实质上都是在user表里控制的
1、grant
#所有的权限 所有数据库下面的所有表 用户 用户ip
grant all on *.* to 'andashu'@'localhost' IDENTIFIED BY '123456' with grant option;
密码 #有执行grant语句的权限
grant all on *.* to 'andashu'@'%' IDENTIFIED BY '123456' with grant option;
取消授权：
Revoke select on *.* from dba@localhost;
Revoke all on *.* from andashu@localhost;

2、修改user表的数据
对user表进行增加、修改和删除
flush privileges;#刷新权限
备份数据库：
mysqldump -uroot -p123456 db > db.sql
mysqldump -uroot -p123456 -A > all.sql
恢复数据：
mysql -uroot -p123456 db < db.sql
存储过程：
批量的造数据
delimiter $$; #为了改结束符
CREATE PROCEDURE big_data1(num int)#代表要造多少条数据 100
BEGIN
DECLARE i int;
set i=0;
WHILE i<num do
insert into students (stu_name,money) VALUES (CONCAT('小明',i),20000);
#CONCAT的作用是连接不同类型的数据
#把字符串和数字拼接到一起
set i=i+1;
end WHILE;
End
$$;
delimiter;

call big_data1(500); #调用
'''