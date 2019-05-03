import copy
'''
1.Python的中拷贝
'''
a = [1, 2, 3, ]
b = a
b.append(4)
print(id(a), a)
print(id(b), b)
# 1329502827400 [1, 2, 3, 4]
# 1329502827400 [1, 2, 3, 4]
# 用id()函数来查看对象的唯一识别号,发现a,b是一样的,
# 原因是因为b只是a的引用，都是同一个地址，并没有实现真正的copy

# 怎么解决呢,如果你想修改一个对象，但是又不需要改动原对象,必须要引入copy模块
a = [1, 2, 3]
b = copy.copy(a)
b.append(4)
print('a:', a)
print('b:', b)
# a: [1, 2, 3]
# b: [1, 2, 3, 4]
# 当然若你已经知道了拷贝对象的类型，对于列表L,直接list(L)做浅拷贝,或者L[:],
#                                   对于字典d,调用dict(d),对于集合拷贝集合s,调用set(s)

'''
2.如何把字典的缺省值为100  {}.fromkeys
'''
aDict = {}.fromkeys(('aa', 'bb', 'cc'), 100)
for k, v in aDict.items():
    print(k, v)
# aa 100
# bb 100
# cc 100

'''
3.如何让列表中的元素存在就返回，不存在就返会默认值  L.get(i,v)
'''
# 你有一个列表L，一个索引号i, 有的时候我们希望当i是L的有效索引时获取L[i],
# 若不是有效索引，返会一个默认值v,其实这个问题若是字典很容易用L.get(i,v)
d = {1: 'aa', 2: 'bb', 3: 'cc'}
print(d.get(4, 'xx'))
# xx
# xx 就是返回的默认值

# 列表怎么破，解决方案#列表的下标是负数的[-len,len),切记切记


def list_get(L, i, v=None):
    if -len(L) <= i <= len(L):
        return L[i]
    else:
        return v


print(list_get([1, 2, 3], -3, None))
print(list_get([1, 2, 3], 5, None))
# 1
# None

'''
4.循环访问序列中的元素和索引
'''
# 我们需要循环访问一个序列并且每一步都知道自己已经访问到的索引，
# 并替换掉对应的值因为Python默认的循环方式是完全不依赖索引的
# 比如我们要把列表中的10替换成3,解决方案:
list1 = [1, 2, 10, 4]
for index, item in enumerate(list1):
    if item > 9:
        list1[index] = 3
print(list1)
#[1, 2, 3, 4]
# 或者直接变成字典去处理: dict(enumerate(list1))
list1 = [1, 2, 10, 4]
list1_dict = dict(enumerate(list1))
list1_dict[2] = 3  # 改变值
print(list(list1_dict.values()))
# [1, 2, 3, 4]
list1_dict['2'] = 3  # 添加值
print(list(list1_dict.values()))
# [1, 2, 3, 4, 3]

'''
5.如何用字典格式化长的字符串 %(dict.value())s
'''
aInfo = {'Wangdachui': 3000, 'NiuYun': 2000, 'LinLing': 4500, 'Tianqi': 8000}
template = '''
Welcome to the pay wall.
NiuYun' salary is %(NiuYun)s.
Wangdachui's salary is %(Wangdachui)s.
'''
print(template % aInfo)
# Welcome to the pay wall.
# NiuYun' salary is 2000.
# Wangdachui's salary is 3000.

'''
6.字典的更新  update
'''
# 一般用在已经设定好了数据结构，比如股票的信息(股票的价格的变动)，工资单啊(工资的变动，人员的增加)，
# key一般不变，只是变value，一招非常实用
aInfo = {'Wang': 3000, 'NiuYun': 2000, 'Lin': 4500, 'Tianqi': 8000}
bInfo = {'Wang': 4000, 'NiuYun': 8000, 'Ming': 3300}
aInfo.update(bInfo)
print(aInfo)
# {'Wang': 4000, 'NiuYun': 8000, 'Lin': 4500, 'Tianqi': 8000, 'Ming': 3300}

'''
7,删除字典
'''
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict['Name']  # 删除键 'Name'
print(dict)
# {'Age': 7, 'Class': 'First'}
dict.clear()     # 清空字典
print(dict)
# {}
del dict         # 删除字典
print(dict)
# <class 'dict'>

'''
8.集合里面的常用的内置函数
'''
# 主要用作判断差,补,类似运算符<,>,|,&
aset = set("sunrise")
bset = set("sunset")
print(aset.issubset(bset))  # 判断集合的所有元素是否都包含在指定集合中
# False
print(aset.intersection(bset))  # 交集
# {'u', 'e', 'n', 's'}
print(aset.difference(bset))  # 差集， aset - bset
# {'i', 'r'}

'''
9.打印文件夹中英文混合的文件

|---abc.txt---
|---test123.txt
|---大家好
for name in os.listdir('.'):
	print(name.decode('gbk'))#win下的中文编码都是gbk
'''
'''
10.找到两个字典的相同的内容
'''
d1 = {"aa": 10, "bb": 20, "cc": 30}
d2 = {"dd": 50, "cc": 30}
print(set(d1.items()))
# {('aa', 10), ('bb', 20), ('cc', 30)}
print(set(d2.items()))
# {('cc', 30), ('dd', 50)}
print(set(d1.items()) & set(d2.items()))
# {('cc', 30)}
print(dict(set(d1.items()) & set(d2.items())))
# {'cc': 30}
