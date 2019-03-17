# 内置函数的高阶
'''1,map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。(经常和lambda匿名函数搭配使用)'''
map_list = map(lambda x: x + 2, [2, 4, 6])
print(map_list)
# <map object at 0x000001DC8B937240>
# map()传入的第一个参数是匿名函数lambda，即函数对象本身。由于结果map_list是一个Iterator(迭代器)，Iterator(迭代器)是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(map_list))
# [4, 6, 8]

# 写一个循环（for也是一个迭代器）作用类似下面
def f(x):
    return x + 2
map_list = []
for n in [2, 4, 6]:
    map_list.append(f(n))
print(map_list)
# [4, 6, 8]

'''2,再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数
    reduce把结果继续和序列的下一个元素做累积计算'''

from functools import reduce
def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))
# 25

'''3,filter()函数用于过滤序列。'''
'''filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。'''
print(list(filter(lambda x: x > 9, [1, 2, 4, 5, 6, 9, 10, 15])))
# [10, 15]

'''4,sorted 排序    sorted(iterable, /, *, key=None, reverse=False)
                    立即返回一个新的列表，对一个可迭代对象的所有元素排序。
                    key: 排序规则为key定义的函数
                    reverse: 表示是否进行翻转排序
'''
sorted([36, 6, -12, 9, -22])  # 列表排序
# [-22, -12, 6, 9, 36]
sorted([36, 6, -12, 9, -22], key=abs)  # 高阶函数，以绝对值大小排序
# [6, 9, -12, -22, 36]
sorted(['bob', 'about', 'Zoo', 'Credit'])  # 字符串排序，按照ASCII的大小排序
# ['Credit', 'Zoo', 'about', 'bob']
# 如果需要排序的是一个元组，则需要使用参数key，也就是关键字。
a = [('b',2), ('a',1), ('c',0)]
list(sorted(a, key=lambda x: x[1]))  # 按照元组第二个元素排序
# [('c', 0), ('a', 1), ('b', 2)]
list(sorted(a, key=lambda x: x[0]))  # 按照元组第一个元素排序
# [('a', 1), ('b', 2), ('c', 0)]
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  # 忽略大小写排序
# ['about', 'bob', 'Credit', 'Zoo']
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)  # 反向排序
# ['Zoo', 'Credit', 'bob', 'about']

'''
5. zip()　　将对象逐一配对
                zip(*iterables)
                从参数中的多个迭代器取元素组合成一个新的迭代器
                返回：一个zip对象，其内部元素为元组；可以转化成列表或元组
                传入参数：元组、列表、字典等迭代器
'''
# 5.1 当zip()函数中只有一个参数时，zip(iterable)从迭代器中依次取一个元组，组成一个元组。
# zip()函数单个参数
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
print(type(tuple1))
# <class 'zip'>
print(list(tuple1))
# [(1,), (2,), (3,), (4,)]

# 5.2当zip()函数有两个参数时，zip(a,b)函数分别从a和b中取一个元素组成元组，再次将组成的元组组合成一个新的迭代器。a与b的维数相同时，正常组合对应位置的元素。当a与b行或列数不同时，取两者中的最小的行列数。
# zip()函数有两个参数
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
p = [[1, 1, 1], [2, 2, 2]]
print(list(zip(m, n)))
# [([1, 2, 3], [1, 1, 1]), ([4, 5, 6], [2, 2, 3]), ([7, 8, 9], [3, 3, 3])]
print(list(zip(m, p)))
# [([1, 2, 3], [1, 1, 1]), ([4, 5, 6], [2, 2, 2])]


# 5.3、zip()函数的应用(************重点***********)
# 矩阵相加减、点乘（也可以用for循环+列表推导式实现）
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
# 矩阵的点乘
print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])
# [1, 2, 3, 8, 10, 18, 21, 24, 27]
# 矩阵相加
print([x+y for a, b in zip(m, n) for x, y in zip(a, b)])
# [2, 3, 4, 6, 7, 9, 10, 11, 12]

'''
另外、*zip(*iterables)函数详解
*zip()函数是zip()函数的逆过程，将zip对象变成原先组合前的数据。
In [24]: m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
In [25]: n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
In [26]: print(*zip(m, n))
([1, 2, 3], [1, 1, 1]) ([4, 5, 6], [2, 2, 3]) ([7, 8, 9], [3, 3, 3])
In [27]: m2, n2 = zip(*zip(m,n))
In [28]: m == list(m2) and n == list(n2)
Out[28]: True
'''