'''
1,Series
'''
import numpy as np
import pandas as pd
#下面是创建Series的三种方法
#方法1：
s1 = pd.Series([1,2,3,4])
#方法2：
s2 = pd.Series(np.arange(10)) # 通过numpy.arange创建
#方法3：
s3 = pd.Series({'1':1,'2':2,'3':3}) # 通过字典创建
s1.values # 查看值
s1.index # 查看索引
s4 = pd.Series([1,2,3,4],index=['A','B','C','D']) # 设置索引
s4.to_dict() # 转化成字典
pd.isnull(s4) #判断其中元素是否为NaN，pd.notnull()同理

'''
2,DataFrame
'''
from pandas import Series,DataFrame
#通过粘贴板导入dataframe
df = pd.read_clipboard() # 在此之前需要你copy一个表
df.columns  # 输出列名
# df.'列名'  # 输出列的数值(是一个Series)
df_new = DataFrame(df,columns=['列名1','列名2'])
s1 = pd.Series(df['列名'])  # 输出这一列，dataframe的每一列是一个series
# s1.index\values     即对series操作，或者通过s1['索引值']

'''
IO操作
1、从粘贴板读取
    df1 = pd.read_clipboard()
    df1.to_clipboard() # 写入粘贴板
2、CSV文件
    df1.to_csv('名字.csv',index=False) # false则表示不添加索引号
    df2 = pd.read_csv('df1.csv') # 读取CSV文件
3、json
    df1.to_json() # 转化成json文件
    pd.read_json(df1.to_json()) # 读取json文件
4、html
    df1.to_html('df1_html') # 转换成HTML文件
5、excel
    df1.to_excel('df1.xlsx') # 生成Excel文件
'''