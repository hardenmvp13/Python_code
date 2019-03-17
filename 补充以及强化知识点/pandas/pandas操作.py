import pandas as pd
import numpy as np

'''
1,导入数据：
pd.read_csv(filename)：从CSV文件导入数据
pd.read_table(filename)：从限定分隔符的文本文件导入数据
pd.read_excel(filename)：从Excel文件导入数据
pd.read_sql(query, connection_object)：从SQL表/库导入数据
pd.read_json(json_string)：从JSON格式的字符串导入数据
pd.read_html(url)：解析URL、字符串或者HTML文件，抽取其中的tables表格
pd.read_clipboard()：从你的粘贴板获取内容，并传给read_table()
pd.DataFrame(dict)：从字典对象导入数据，Key是列名，Value是数据
'''

'''
2,df.to_csv(filename)：导出数据到CSV文件
df.to_excel(filename)：导出数据到Excel文件
df.to_sql(table_name, connection_object)：导出数据到SQL表
df.to_json(filename)：以Json格式导出数据到文本文件
'''

'''
3,创建测试对象：
'''
# 创建20行5列的随机数组成的DataFrame对象
df = pd.DataFrame(np.random.rand(5,3))
print(df)
#           0         1         2
# 0  0.490465  0.427390  0.677877
# 1  0.470189  0.229135  0.360828
# 2  0.832371  0.894718  0.725593
# 3  0.730699  0.189548  0.309905
# 4  0.934741  0.983374  0.701640

# 从可迭代对象my_list创建一个Series对象
# pd.Series(my_list)
# ：增加一个日期索引
# df.index = pd.date_range('1900/1/30', periods=df.shape[0])

'''
4,查看、检查数据：
'''
n = 1
df.head(n)          #：查看DataFrame对象的前n行
df.tail(n)          #：查看DataFrame对象的最后n行
df.shape()          #：查看行数和列数
df.info()           #：查看索引、数据类型和内存信息
df.describe()       #：查看数值型列的汇总统计
df.value_counts(dropna=False)           #查看Series对象的唯一值和计数
df.apply(pd.Series.value_counts)        #：查看DataFrame对象中每一列的唯一值和计数

'''
5,数据选取：
df[col]：根据列名，并以Series的形式返回列
df[[col1, col2]]：以DataFrame形式返回多列
s.iloc[0]：按位置选取数据
s.loc['index_one']：按索引选取数据
df.iloc[0,:]：返回第一行
df.iloc[0,0]：返回第一列的第一个元素
'''

'''
6,数据统计：

复制代码
df.describe()：查看数据值列的汇总统计
df.mean()：返回所有列的均值
df.corr()：返回列与列之间的相关系数
df.count()：返回每一列中的非空值的个数
df.max()：返回每一列的最大值
df.min()：返回每一列的最小值
df.median()：返回每一列的中位数
df.std()：返回每一列的标准差
'''

'''
7,数据合并：

df1.append(df2)：将df2中的行添加到df1的尾部
df.concat([df1, df2],axis=1)：将df2中的列添加到df1的尾部
df1.join(df2,on=col1,how='inner')：对df1的列和df2的列执行SQL形式的join
'''

'''
8,数据处理：

复制代码
df[df[col] > 0.5]：选择col列的值大于0.5的行
df.sort_values(col1)：按照列col1排序数据，默认升序排列
df.sort_values(col2, ascending=False)：按照列col1降序排列数据
df.sort_values([col1,col2], ascending=[True,False])：先按列col1升序排列，后按col2降序排列数据
df.groupby(col)：返回一个按列col进行分组的Groupby对象
df.groupby([col1,col2])：返回一个按多列进行分组的Groupby对象
df.groupby(col1)[col2]：返回按列col1进行分组后，列col2的均值
df.pivot_table(index=col1, values=[col2,col3], aggfunc=max)：创建一个按列col1进行分组，并计算col2和col3的最大值的数据透视表
df.groupby(col1).agg(np.mean)：返回按列col1分组的所有列的均值
data.apply(np.mean)：对DataFrame中的每一列应用函数np.mean
data.apply(np.max,axis=1)：对DataFrame中的每一行应用函数np.max
'''

'''
9,数据清理：

复制代码
df[df[col] > 0.5]：选择col列的值大于0.5的行
df.sort_values(col1)：按照列col1排序数据，默认升序排列
df.sort_values(col2, ascending=False)：按照列col1降序排列数据
df.sort_values([col1,col2], ascending=[True,False])：先按列col1升序排列，后按col2降序排列数据
df.groupby(col)：返回一个按列col进行分组的Groupby对象
df.groupby([col1,col2])：返回一个按多列进行分组的Groupby对象
df.groupby(col1)[col2]：返回按列col1进行分组后，列col2的均值
df.pivot_table(index=col1, values=[col2,col3], aggfunc=max)：创建一个按列col1进行分组，并计算col2和col3的最大值的数据透视表
df.groupby(col1).agg(np.mean)：返回按列col1分组的所有列的均值
data.apply(np.mean)：对DataFrame中的每一列应用函数np.mean
data.apply(np.max,axis=1)：对DataFrame中的每一行应用函数np.max
'''

'''
10,改列名：
方法1
a.columns = ['a','b','c']
方法2
a.rename(columns={'A':'a', 'B':'b', 'C':'c'}, inplace = True)
'''

'''
11,Pandas.DataFrame插入列和行
https://www.jianshu.com/p/7df2593a01ce
'''