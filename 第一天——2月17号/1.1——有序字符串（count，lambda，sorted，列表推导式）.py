from collections import Counter
'''
1.有序字符数

计算每个字符的出现次数，并按照出现的顺序将其作为元组列表返回。

例如给你一个字符串"abracadabra"，统计里面的字符按照下面的格式输出:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

'''
# 自己写的代码

'''
没有排序
'''


def ordered_count():
    string = str(input("请输入字符串："))
    count_resoult = {}  # 字典
    for i in set(string):  # 引入set，利用集合进行去重，减少计算量
        count_resoult[i] = string.count(i)
    print(count_resoult.items())


# ordered_count()
'''
运行结果：
dict_items([('a', 5), ('d', 1), ('b', 2), ('r', 2), ('c', 1)])
{('a', 5), ('b', 2), ('r', 2), ('d', 1), ('c', 1)}
'''


# 1.1群主的代码（用count）
def ordered_count1(s):
    results = set()  # 新建一个空白集合,去除重复字母
    for i in s:
        results.add((i, s.count(i)))
    print(sorted(list(results), key=lambda x: x[1], reverse=True))


s = "abracadabra"
ordered_count1(s)

'''
运行结果：
[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]

'''
'''
##################补充知识#########################
（一）sorted函数：
    sorted(iterable[, cmp[, key[, reverse]]])

    iterable -- 可迭代对象。
    cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

    示例：
    l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
    sorted(l, key=lambda x:x[0], reverse=True)
    输出;[('e', 3), ('d', 4), ('c', 6), ('b', 2), ('a', 1)]

（二）匿名函数：lambda
lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
add = lambda x, y : x+y
add(1,2)  # 结果为3

'''

# 1.2群主的代码（用count，并且使用列表推导式）


def ordered_count2(s):
    #results = [(i,s.count(i)) for i in s]
    # 输出结果：[('a', 5), ('b', 2), ('r', 2), ('a', 5), ('c', 1), ('a', 5), ('d', 1), ('a', 5), ('b', 2), ('r', 2), ('a', 5)]
    #results = set([(i, s.count(i)) for i in s])
    # 输出结果：{('c', 1), ('d', 1), ('b', 2), ('r', 2), ('a', 5)}    是一个集合
    results = list(set([(i, s.count(i)) for i in s]))
    # 输出结果：[('b', 2), ('c', 1), ('r', 2), ('d', 1), ('a', 5)]    变成列表，但是还没有排序
    print(sorted(results, key=lambda x: x[1], reverse=True))
    # 输出结果为：[('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]


s = "abracadabra"
ordered_count2(s)

'''
运行结果：[('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
'''

# 3  使用collections


def ordered_count3(str):
    results = [(key, values) for key, values in dict(Counter(str)).items()]
    print(sorted(results, key=lambda x: x[1], reverse=True))


ordered_count3('abracadabra')

'''
运行结果：
[('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
'''

# 4，使用字典
