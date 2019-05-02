'''
1.字典的排序:
'''
# 1.1 用万金油sorted()函数

my_dict={"cc":100,"aa":200,"bb":10}
print(sorted(my_dict.items(),key=lambda x:x[0]))#表示按照key排序
# >>>[('aa', 200), ('bb', 10), ('cc', 100)]
print(sorted(my_dict.items(),key=lambda x:x[1]))#表示按照value排序
# >>>[('bb', 10), ('cc', 100), ('aa', 200)]
# 注意原始的my_dict本身顺序并没有变(不信你可以print看看),排序是通过sorted()返回了一个新的字典
print(my_dict)
# {'cc': 100, 'aa': 200, 'bb': 10}

# 1.2另外一种做法, 因为字典是无序，若你一开始设计的时候就希望这个数据结构，
#    按照的添加的顺序进行有序排列(比如读取CSV文件)，那么我们就是利用collection模块里面的OrderedDict()处理:
from collections import OrderedDict
orderDict = OrderedDict()
orderDict['a'] = 1
orderDict['b'] = 2
orderDict['c'] = 3
print(orderDict)
# >>>OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 对比一下，若是普通的dict是乱序的，若不用OrderedDict()
orderDict=dict()
orderDict['a']=1
orderDict['b']=2
orderDict['c']=3
print(orderDict)
# >>>{'a': 1, 'c': 3, 'b': 2}
# 最后要提醒一下:OrderedDict()虽然是好东西，但是它内部维护了一个双向链表,若数据量很大的话，会非常消耗内存.

'''
2.字典的取值

字典中取值大家很容易想到用dict[key],这个有什么难的，确实一般取值是这样的,
但是你有没有想过若你取的值不存在，就会发生异常,风险很大.(良好的代码，一定是要考虑健壮性,切记)
建议:尽量用dict.get()来代替dict[key]
'''

prices = {'apple':10,'orange':5,'banana':15}
print(prices['apple'])
# 10
# print(prices['peach'])
# KeyError: 'peach'
# 因为试图通过索引的方式去取值,比如dict[key],当key不是字典dict的键，会引起异常，
# 有没有什么两全的办法有值的时候取值，没有值的时候即使我取不到也不会发生异常

# 答案是有的，python早就给你准备好了.我们用dict.get()
print(prices.get('peach')) #当键值不存在的时候，会返回None,而不是异常
# None
#get还有一个工厂方法，就是dict.get(key,somthingelse)
print(prices.get('peach','Not found'))
# Not found
# 建议:尽量用dict.get()来代替dict[key]

'''
3,字典中提取部分子集
我们原来有一个长的字典，我们想提取其中一部分变成另外一个子集,我们怎么做呢，我们来看一个小例子:
字典推导式
'''
students_score={'jack':80,'james':91,'leo':100,'sam':60}
#提取分数超过90分的学生信息，并变成字典
# 我们可以用字典推导式，轻松搞定
good_score = {name:score for  name,score in students_score.items() if score>90}
print(good_score)
# >>>{'james': 91, 'leo': 100}

'''
4.字典的计算
比如我们有一个字典是记录股票的价格呢，一般key都是股票的名字,而value是价格，
若我们想对价格进行计算，应该如何处理呢,我们还是通过实例来讲解：
'''
# 下面是一个股票价格的字典，我们希望得到里面的最大值，最小值
stocks={'wanke':25.6,'wuliangye':32.3,'maotai':299.5,'huatai':18.6}

# 4.1 利用字典的values
print(min(stocks.values()))
#18.6

# 4.2 利用zip() 内置函数
#      当zip()函数中只有一个参数时，zip(iterable)从迭代器中依次取一个元组，组成一个元组。
new_stocks = zip(stocks.values(),stocks.keys())
print(new_stocks)
print(min(new_stocks))
#(18.6, 'huatai')

'''
5,字典的翻转（值和键翻转过来）
  在处理复杂的数据结构的时候，有的时候希望把字典翻转,一般用推导列表进行过渡，然后再用dict()函数编程字典
'''
stocks={'wanke':25.6,'wuliangye':32.3,'maotai':299.5,'huatai':18.6}
invert_stockd = dict([(v,k) for k,v in stocks.items()])
print(invert_stockd)
#{25.6: 'wanke', 32.3: 'wuliangye', 299.5: 'maotai', 18.6: 'huatai'}

