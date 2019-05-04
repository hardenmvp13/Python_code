'''
基本查询：SELECT * FROM <表名>

条件查询：SELECT * FROM students WHERE score >= 80;  “分数在80分或以上的学生”
          SELECT * FROM students WHERE score >= 80 AND gender = 'M';    “分数在80分或以上”，并且还符合条件“男生”，
          SELECT * FROM students WHERE score >= 80 OR gender = 'M';     “分数在80分或以上”或者“男生”，满足任意之一的条件”
          SELECT * FROM students WHERE NOT class_id = 2;                “不是2班的学生”
          SELECT * FROM students WHERE (score < 80 OR score > 90) AND gender = 'M';     “分数在80以下或者90以上，并且是男生”

投影查询：使用SELECT *表示查询表的所有列，使用SELECT 列1, 列2, 列3则可以仅返回指定列，这种操作称为投影
          SELECT id, score points, name FROM students;      SELECT语句将列名score重命名为points，而id和name列名保持不变

排序：SELECT id, name, gender, score FROM students ORDER BY score;     按照成绩从低到高进行排序
      SELECT id, name, gender, score FROM students ORDER BY score DESC; 按照成绩从高到底排序，我们可以加上DESC表示“倒序”
      SELECT id, name, gender, score FROM students ORDER BY score DESC, gender; 使用ORDER BY score DESC, gender表示先按score列倒序，如果有相同分数的，再按gender列排序：

分页查询：把结果集分页，每页3条记录。要获取第1页的记录，可以使用LIMIT 3 OFFSET 0
        SELECT id, name, gender, score
        FROM students
        ORDER BY score DESC
        LIMIT 3 OFFSET 0;

聚合查询：SELECT COUNT(*) num FROM students;使用聚合查询时，我们应该给列名设置一个别名，便于处理结果
        SUM	计算某一列的合计值，该列必须为数值类型
        AVG	计算某一列的平均值，该列必须为数值类型
        MAX	计算某一列的最大值
        MIN	计算某一列的最小值

多表查询：
        SELECT
            students.id sid,
            students.name,
            students.gender,
            students.score,
            classes.id cid,
            classes.name cname
        FROM students, classes;

连接查询：
        （1），内连接
        SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
        FROM students s
        INNER JOIN classes c
        ON s.class_id = c.id;
        （2），
        外连接，右
        SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
        FROM students s
        RIGHT OUTER JOIN classes c
        ON s.class_id = c.id;
        外连接，左
        SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
        FROM students s
        LEFT OUTER JOIN classes c
        ON s.class_id = c.id;
        （3），都存在
        SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
        FROM students s
        FULL OUTER JOIN classes c
        ON s.class_id = c.id;

区别：我们把tableA看作左表，把tableB看成右表，
        那么INNER JOIN是选出两张表都存在的记录：
        LEFT OUTER JOIN是选出左表存在的记录：
        RIGHT OUTER JOIN是选出右表存在的记录：
        FULL OUTER JOIN则是选出左右表都存在的记录：
'''
'''
插入：INSERT INTO <表名> (字段1, 字段2, ...) VALUES (值1, 值2, ...);
      INSERT INTO students (class_id, name, gender, score) VALUES (2, '大牛', 'M', 80);
      INSERT INTO students (class_id, name, gender, score) VALUES
          (1, '大宝', 'M', 87),
          (2, '二宝', 'M', 81);
          
'''
'''
更新：UPDATE <表名> SET 字段1=值1, 字段2=值2, ... WHERE ...;
      UPDATE students SET name='大牛', score=66 WHERE id=1;   更新id=1的记录
      UPDATE students SET name='小牛', score=77 WHERE id>=5 AND id<=7;    更新id=5,6,7的记录
      UPDATE students SET score=score+10 WHERE score<80;    更新score<80的记录
'''
'''
删除：DELETE FROM <表名> WHERE ...;
    DELETE FROM students WHERE id=1;    删除id=1的记录
    DELETE FROM students WHERE id>=5 AND id<=7; 删除id=999的记录
'''