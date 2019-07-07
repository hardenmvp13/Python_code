import collections

'''1, namedtuple'''
'''
来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
'''
from collections import namedtuple
point = namedtuple('point', ['x', 'y'])
p = point(2, 3)
print(p.x)
# 2
print(p.y)
# 3

'''2, deque'''
'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
'''
from collections import deque
e_list = ['a', 'b', 'c']
e_list_new = deque(e_list)
e_list_new.appendleft('harden')
print(e_list_new)
# deque(['harden', 'a', 'b', 'c'])

'''3,defaultdict '''
'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
    除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
from collections import defaultdict
dd_list = defaultdict(lambda: "harden")
dd_list['key1'] = 'james'
print(dd_list['key1']) # key1存在
# james
print(dd_list['key2']) # key2不存在，返回默认值
# harden

'''4,OrderedDict    保持Key的顺序'''
'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict
'''
from collections import OrderedDict
od_dict = dict([("harden", 13), ("james", 23), ("curry", 30), ("adun", 33)])
print(od_dict)
# {'harden': 13, 'james': 23, 'curry': 30, 'adun': 33}
odd_dict = OrderedDict([("harden", 13), ("james", 23), ("curry", 30), ("adun", 33)])
print(odd_dict)
OrderedDict([('harden', 13), ('james', 23), ('curry', 30), ('adun', 33)])
print(type(odd_dict))
# <class 'collections.OrderedDict'>

'''5,Counter 简单的计数器'''
from collections import Counter
c = Counter('harden')
# c = Counter({'a': 4, 'b': 2})
print(c)

