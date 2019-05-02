'''
列表：13招操作
      这个是python里面用的最多最常用的数据类型，可以通过下标来访问，可以理解为java或者c里面的数组.
      但是功能比数组强大n倍,list可以放任意数量的python对象，
      可以是字符串，字符，整数，浮点等等都可以，而且创建，添加，删除也很方便.
'''

# (1),创建list   list内部的对象可以是字符串，字符，数字，支持混搭
aList = ['apple', 100, 0.01, 'banana', 'A', 'B', 'C']

# (2)访问list    直接通过下标去访问
print(aList[0])
# apple

# (3),列表的切片 通过切片来取列表中的一部分
print(aList[4:6])
# ['A', 'B']

# (4),列表的嵌套     列表支持嵌套，就是列表里面可以套列表，甚至套字典，元组等
bList=[100,200,['aaa','bbb','ccc']]
print(bList[2][0])
# aaa

# (5)列表的插入  内置函数append,insert
alist = ['a',10,15,'b','c','d']
alist[1] = 'f'
print(alist)
# ['a', 'f', 15, 'b', 'c', 'd']

alist.append('e')
print(alist)
# ['a', 'f', 15, 'b', 'c', 'd', 'e']

alist.insert(2,'g')
print(alist)
# ['a', 'f', 'g', 15, 'b', 'c', 'd', 'e']

# (6),列表的删除     内置remove,pop函数
# 如果知道要删除对象在列表的里面的位置，比如'a'在alist = ['a',10,15,'b','c','d']的第0个位置
alist = ['a',10,15,'b','c','d']
del alist[0]
print(alist)
# [10, 15, 'b', 'c', 'd']

# 如果不知道位置，只是要删除某个对象
alist.remove('b')
print(alist)
# [10, 15, 'c', 'd']

# 如果要删除队尾的
alist.pop()
print(alist)
# [10, 15, 'c']

# (7),列表支持*，+
list1=[1,2,3]
list2=[100,200,300]
list3=list1+list2
print(list3)
# [1, 2, 3, 100, 200, 300]

list4=['a','b','c']
list5=list4*3
print(list5)
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

# (8)列表的排序//内置了sort函数非常方便,通过传入reverse为True或者False来升序或者降序排列
blist = [2,65,2,3,56,23,5622,-5,226,89]
blist.sort(reverse=True)
print(blist)
# [5622, 226, 89, 65, 56, 23, 3, 2, 2, -5]
blist.sort(reverse=False) #默认升序
print(blist)
# [-5, 2, 2, 3, 23, 56, 65, 89, 226, 5622]

# (9)计算列表的长度 //利用内置函数len()
aList=[1,2,3,4,5]
print(len(aList))
# 5

# (10),计算列表里面的最大值，最小值
aList=[1,2,3,4,5]
print(min(aList))
# 1
print(max(aList))
# 5
# 当然你若要想知道，最大的前2个数，或者最小的2个数，需要用heapq模块,以后在python黑魔法里面会详细讲.


# (11),列表的扩展 //用内置extend函数，看起来和+差不多，其实区别在于+是返回一个新的列表，而extend是直接修改了列表
aList=[1,2,3]
b=[4,5,6]
aList.extend(b)
print(aList)
# [1, 2, 3, 4, 5, 6]

# (12),查找列表中某一个元素的索引//内置函数index
aList=['This','is','a','very','good','idea']
print(alist.index('very'))
# 3

# (13),统计某个元组在列表里面的次数,内置函数count
aList=['to','do','or','not','to','do']
print(aList.count('to'))
# 2

'''
元组：元组和列表一样，也是一种序列，唯一的不同在于不能修改
1）元组的创建
aTuple=(1,2,3)
print(aTuple)
>>>(1, 2, 3)
有一点要注意，当元组里面只有一个元素的时候，一定要加, 比如(100,)

2)元组的用法和列表一模一样
既然用法和列表一样，为啥还要发明元组，原因在于
有一些特殊的场合需要不可变序列，比如后面会讲道的数据结构字典，必须要用不可变序列作为键值，而列表不行。
有一些内建的函数的返回值，也必须是元组.
'''




