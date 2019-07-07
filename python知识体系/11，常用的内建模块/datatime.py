'''
datatime:处理时间和日期的标准库
'''
'''一，获取当前时间——使用now()方法'''
from datetime import datetime
print(datetime.now())
# 2019-05-08 09:59:25.798865
print(type(datetime.now()))
# <class 'datetime.datetime'>

'''二，获取指定的日期和时间'''
Designation_time = datetime(year=2019, month=5, day=18)
print(Designation_time)
# 2019-05-18 00:00:00

'''三，datetime转换为timetamp——使用timetamp()方法 '''
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
Designation_time = datetime(year=2019, month=5, day=18)
print(Designation_time)
# 2019-05-18 00:00:00
print(Designation_time.timestamp())
# 1558108800.0
print(type(Designation_time.timestamp()))
# <class 'float'>
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

'''四，将timetamp转换成datatime——使用fromtimestamp()'''
Designation_time = datetime(year=2019, month=5, day=18)
Designation_time_timestamp = Designation_time.timestamp()
print('timestamp:', Designation_time_timestamp)
# timestamp: 1558108800.0
print('datatime:', Designation_time.fromtimestamp(Designation_time_timestamp))
# datatime: 2019-05-18 00:00:00

'''五，将str转换成datatime'''
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 2015-06-01 18:19:59

'''六，将datatime转化成str'''
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
# Wed, Jun 05 00:57

