import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', db= 'yangji')
cursor = db.cursor()
sql = 'select * from formula'

cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    # 打印结果
    print("fname=%s,lname=%s,age=%s,sex=%s" % \
          (fname, lname, age, sex))
# print(results)
cursor.close()