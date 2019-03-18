import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''1，创建对象'''
# 1.1 使用传递的值列表序列创建序列, 让pandas创建默认整数索引
s = pd.Series([1,3,5,np.nan,6,8])
# print(s)
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

# 1.2 使用传递的numpy数组创建数据帧,并使用日期索引和标记列.
dates = pd.date_range('20130101',periods=6)
# print(dates)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# print(df)
#                    A         B         C         D
# 2013-01-01  1.329457  0.107822  2.338926  3.244382
# 2013-01-02  0.713496  0.302043  1.292043  0.636480
# 2013-01-03 -0.713168  2.393433 -0.291605  0.403200
# 2013-01-04 -0.146484  0.230842 -0.462589  1.028628
# 2013-01-05 -1.052638 -0.161416  0.261323 -2.023400
# 2013-01-06 -0.518567  0.364021 -0.122270  0.960540

# 1.3 使用传递的可转换序列的字典对象创建数据帧.
df2 = pd.DataFrame({ 'A' : 1.,
                      'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
# print(df2)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo