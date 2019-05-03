'''
###################  python内置函数(常用)  ##################
# 重点  22. eval()  24. filter()  26. format()  42. map()  52. range()  59.sorted()  67,zip()
# sorted()  67. zip()
'''
'''1,abs(x)  取绝对值'''
abs(-10)
# 10

'''2. all()　接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False'''
tmp_1 = ['python', 123]
print(all(tmp_1))
# True
tmp_2 = []
print(all(tmp_2))
# True
tmp_3 = [0]
print(all(tmp_3))
# False

'''3. any()　　接受一个迭代器，如果迭代器里有一个元素为真，那么返回True,否则返回False'''

'''4. ascii()　　调用对象的__repr__()方法，获得该方法的返回值.'''

'''5. bin(),　6. oct(),  7. hex()  　　三个函数功能为：将十进制数分别转换为2/8/16进制。'''

'''8. bool()　　测试一个对象是True还是False.'''

'''9. bytes()　　将一个字符串转换成字节类型'''
s = 'python'
x = bytes(s, encoding='utf-8')
# b'python'
a = '王'
s = bytes(a, encoding='utf-8')
# b'\xe7\x8e\x8b'

''' 10. str()　　将字符类型/数值类型等转换为字符串类型'''
str(b'\xe7\x8e\x8b', encoding='utf-8')  # 字节转换为字符串
# '王'
str(1)   # 整数转换为字符串
# '1'

'''11，challable()　　判断对象是否可以被调用，能被调用的对象就是一个callables对象，比如函数和带有__call__()的实例'''
callable(max)
# True
callable([1, 2, 3])
# False
callable(None)
# False
callable('str')
# False

'''12，char()，13. ord()　　查看十进制数对应的ASCII字符/查看某个ASCII对应的十进制数'''
# chr(-1)
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     chr(-1)
# ValueError: chr() arg not in range(0x110000)
chr(0)
# '\x00'
ord('\x00')
# 0
ord('7')
# 55

'''
14，classmethod()　　用来指定一个方法为类的方法，由类直接调用执行，
                    只有一个cls参数,执行雷的方法时，自动将调用该方法的类赋值给cls.没有此参数指定的类的方法为实例方法
'''
class Province:
    country = "中国"
    def __init__(self, name):
        self.name = name
    @classmethod
    def show(cls):  # 类方法，由类调用，最少要有一个参数cls，调用的时候这个参数不用传值，自动将类名赋值给cls
        print(cls)
# 调用方法
Province.show()

'''
15，complie()　　将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译
                    compile(
    source,
    filename,
    mode,
    flags=0,
    dont_inherit=False,
     optimize=-1)
                    将source编译为代码或者AST对象。代码对象能过通过exec语句来执行或者eval()进行求值。
                       source：字符串或者AST（abstract syntax trees）对象。
                       filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
                       model：指定编译代码的种类。可以指定'exec', 'eval', 'single'。
                       flag和dont_inherit：这两个参数为可选参数。
'''
s = "print('helloworld')"
r = compile(s, "<string>", "exec")
# <code object <module> at 0x000001C648038390, file "<string>", line 1>

'''
16，complex()  创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。
               如果第一个参数是字符串，则不需要指定第二个参数。
                参数real：int，long，float或字符串。
                参数imag：int，long，float。
'''

'''17. delattr()　　删除对象的属性'''

'''18. dict()　　   创建数据字典'''
a = dict()  # 空字典
# {}
b = dict(one=1, two=2)
# {'one': 1, 'two': 2}
c = dict({'one': 1, 'two': 2})
# {'one': 1, 'two': 2}

'''19. dir()　　不带参数时返回当前范围内的变量，方法和定义的类型列表，带参数时返回参数的属性，方法列表'''
dir()
dir(list)  # 查看list方法


'''20. divmod()　　分别取商和余数'''
divmod(20, 6)
# (3, 2)

'''21，enumerate()　　返回一个可以枚举的对象，该对象的next()方法将返回一个元组'''
test = ['a', 'b', 'c']
for k, v in enumerate(test):
    print(k, v)
# 0 a
# 1 b
# 2 c

'''22. eval()　　将字符串str当成有效的表达式来求值并返回计算结果'''
# (1)、简单表达式
print(eval('1+2'))
# 3
# (2)、字符串转字典
print(eval("{'name':'linux','age':18}"))
# {'name':'linux','age':18}
# (3)、传递全局变量
print(eval("{'name':'linux','age':age}", {"age": 1822}))
# {'name': 'linux', 'age': 1822}
# (4)、传递本地变量
age = 18
print(eval("{'name':'linux','age':age}", {"age": 1822}, locals()))
# {'name': 'linux', 'age': 18}
s = "1+2*3"
type(s)
# <class 'str'>
eval(s)
# 7

'''23. exec()　　执行字符串或complie方法编译过的字符串，没有返回值'''

'''
24. filter()　　过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，
              在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据
                filter(function, iterable)
                参数function：返回值为True或False的函数，可以为None。
                参数iterable：序列或可迭代对象。
'''


def bigerthan5(x):
    return x > 5


filter(bigerthan5, [3, 4, 5, 6, 7, 8])
# [6, 7, 8]

'''25. float()　　讲一个字符串或整数转换为浮点数'''
float()
# 0.0
float('123')
# 123.0
float(1)
# 1.0
# float('a')
# Traceback (most recent call last):
#   File "<pyshell#45>", line 1, in <module>
# float('a')
# ValueError: could not convert string to float: 'a'

'''26. format()　　格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法'''
"I am {0}, I like {1}!".format("wang", "moon")
# 'I am wang, I like moon!'

'''
27. frozenset()　　创建一个不可修改的集合
                    frozenset([iterable])
                    set和frozenset最本质的区别是前者是可变的，后者是不可变的。
                                  当集合对象会被改变时（例如删除，添加元素），只能使用set，
                    一般来说使用fronzet的地方都可以使用set。
                    参数iterable：可迭代对象。
'''
'''
28. getattr()　　获取对象的属性
               getattr(object, name [, defalut])
                  获取对象object名为name的特性，如果object不包含名为name的特性，
                  将会抛出AttributeError异常；如果不包含名为name的特性，且提供default参数，将返回default。
                参数object：对象
                参数name：对象的特性名
                参数default：缺省返回值
'''
append = getattr(list, 'append')
append
# <method 'append' of 'list' objects>
mylist = [3, 4, 5]
append(mylist, 6)
mylist
# [3, 4, 5, 6]
# method = getattr(list, 'add')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: type object 'list' has no attribute 'add'
method = getattr(list, 'add', 'NoMethod')
method
# 'NoMethod'

'''29. globals()　　返回一个描述当前全局变量的字典'''
a = 1
globals()
# {'__loader__': <class '_frozen_importlib.BuiltinImporter'>, 'a': 1, '__builtins__': <module 'builtins' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, '__spec__': None}

'''
30. hasattr()    hasattr(object，name)
                判断对象object是否包含名为name的特性（hasattr是通过调用getattr(object，name)）是否抛出异常来实现的。
                参数object：对象
                参数name：特性名称
'''
hasattr(list, 'append')
# True
hasattr(list, 'add')
# False

'''
31. hash()　哈希值   hash(object)
              如果对象object为哈希表类型，返回对象object的哈希值。哈希值为整数，在字典查找中，哈希值用于快递比价字典的键。
              两个数值如果相等，则哈希值也相等。
'''
'''32. help()　　返回对象的帮助文档'''
'''33. id()　　返回对象的内存地址'''
a = 1
id(a)
# 1588522800

'''34. input()　　获取用户输入内容'''
num = input("请输入一个数字：")
# 用户输入3
print(num)
# 输出结果
3

'''35. int()　　将一个字符串或数值转换为一个普通整数'''

'''
36，isinstance()　　检查对象是否是类的对象，返回True或False
                      isinstance(obj, cls)
                      检查obj是否是类cls的对象, 返回True 或 False
'''


class Foo(object):
    pass


obj = Foo()
isinstance(obj, Foo)
# True

'''
37. issubclass()　　检查一个类是否是另一个类的子类。返回True或False
                  issubclass(sub, super)
                  检查sub类是否是super类的派生类（子类）。返回True 或 False
'''


class Foo(object):
    pass


class Bar(Foo):
    pass


issubclass(Bar, Foo)
# True

'''
42. map()     并行遍历，可接受一个function类型的参数
                map(function, iterable,...)
                对于参数iterable中的每个元素都应用fuction函数，并将结果作为列表返回。
                如果有多个iterable参数，那么fuction函数必须接收多个参数，这些iterable中相同索引处的元素将并行的作为function函数的参数。
                如果一个iterable中元素的个数比其他少，那么将用None来扩展改iterable使元素个数一致。
                如果有多个iterable且function为None，map()将返回由元组组成的列表，每个元组包含所有iterable中对应索引处值。
                参数iterable必须是一个序列或任何可遍历对象，函数返回的往往是一个列表(list)。
'''
a = [1, 3, 5]
b = [2, 4, 6]
map(None, a, b)
# [(1, 2), (3, 4), (5, 6)]
map(lambda x, y: x * y, a, b)
# [2, 12, 30]
li = [1, 2, 3]
data = map(lambda x: x * 100, li)
print(type(data))
data = list(data)
print(data)
# <class 'map' >
# [100, 200, 300]

'''43. max()　　返回给定元素里最大值'''

'''44. meoryview()'''

'''45. min()　　返回给定元素里最小值'''

'''46. next()　　返回一个可迭代数据结构（如列表）中的下一项'''

'''
47. object()  获取一个新的，无特性(geatureless)对象。Object是所有类的基类。它提供的方法将在所有的类型实例中共享。
            该函数时2.2.版本新增，2.3版本之后，该函数不接受任何参数。
'''

'''
48. open()　　打开文件
            open(filename[, mode[, bufsize]])
'''

'''49. pow()　　幂函数'''
r = pow(2, 10)  # 2的10次方
print(r)
# 1024

'''50，print()　　输出函数'''

'''51. property() '''

'''
  52. range()　　根据需要生成一个指定范围的数字，可以提供你需要的控制来迭代指定的次数
                  用于创建包含连续算术值的列表(list)。常用于for循环。参数必须是普通整数。
                参数step默认值为1，参数start的默认值为0。
                全参数调用该函数将返回一个普通整数列表。
                step 可以是正整数或者负整数。不可以为0，否则将处罚ValueError异常。
                range(3)代表0,1,2.等价于range(0,3)
'''
range(0, 10, 2)  # 第一个参数是起始数，第二个是终止数(不包含这个)，第三个数步数
# [0,2,4,6,8]

'''
53. repr()　　将任意值转换为字符串，供计时器读取的形式
              repr(object)
             返回一个对象的字符串表示。有时可以使用这个函数来访问操作。
             对于许多类型来说，repr()尝试返回一个字符串，eval()方法可以使用该字符串产生对象；
             否则用尖括号括起来的，包含类名称和其他二外信息的字符串被返回。
'''

'''
54. reversed()　　　反转，逆序对象
                    reversed(seq)
             返回一个逆序的iterator对象。参数seq必须是一个包含__reversed__()方法的对象或支持序列操作(__len__()和__getitem__())
             该函数是2.4中新增的
'''

'''
55. round()　　四舍五入
           round(x [, n])
            对参数x的第n+1位小数进行四舍五入，返回一个小数位数为n的浮点数。
            参数n的默认值是0。结果是一个浮点数。如round(0.5)结果为1.0
'''
round(4, 6)
# 4
round(5, 6)
# 5

'''56. set()'''

'''57. setattr()　　与getattr()相对应'''


'''58. slice()　　切片功能 '''

'''
59. sorted()　　排序
                sorted(iterable, /, *, key=None, reverse=False)
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
a = [('b', 2), ('a', 1), ('c', 0)]
list(sorted(a, key=lambda x: x[1]))  # 按照元组第二个元素排序
# [('c', 0), ('a', 1), ('b', 2)]
list(sorted(a, key=lambda x: x[0]))  # 按照元组第一个元素排序
# [('a', 1), ('b', 2), ('c', 0)]
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)             # 忽略大小写排序
# ['about', 'bob', 'Credit', 'Zoo']
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)  # 反向排序
# ['Zoo', 'Credit', 'bob', 'about']

'''60. staticmethod()'''

'''61. str()　　字符串构造函数'''

'''62. sum()　　求和'''

'''63. super()　　调用父类的方法'''

'''64. tuple()　　元组构造函数'''

'''65. type()　　显示对象所属的类型'''

'''66. vars()　　'''

'''
67. zip()　　 将对象逐一配对
              zip(*iterables)
                从参数中的多个迭代器取元素组合成一个新的迭代器
                返回：一个zip对象，其内部元素为元组；可以转化成列表或元组
                传入参数：元组、列表、字典等迭代器
'''
# 67.1 当zip()函数中只有一个参数时，zip(iterable)从迭代器中依次取一个元组，组成一个元组。
# zip()函数单个参数
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
type(tuple1)
# zip
list(tuple1)
# [(1,), (2,), (3,), (4,)]

# 67.2当zip()函数有两个参数时，zip(a,b)函数分别从a和b中取一个元素组成元组，再次将组成的元组组合成一个新的迭代器。a与b的维数相同时，正常组合对应位置的元素。当a与b行或列数不同时，取两者中的最小的行列数。
# zip()函数有两个参数
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
p = [[1, 1, 1], [2, 2, 2]]
list(zip(m, n))
# [([1, 2, 3], [1, 1, 1]), ([4, 5, 6], [2, 2, 3]), ([7, 8, 9], [3, 3, 3])]
list(zip(m, p))
# [([1, 2, 3], [1, 1, 1]), ([4, 5, 6], [2, 2, 2])]

# 67.3、zip()函数的应用
# 矩阵相加减、点乘（也可以用for循环+列表推导式实现）
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
# 矩阵的点乘
[x * y for a, b in zip(m, n) for x, y in zip(a, b)]
# [1, 2, 3, 8, 10, 18, 21, 24, 27]
# 矩阵相加
[x + y for a, b in zip(m, n) for x, y in zip(a, b)]
# [2, 3, 4, 6, 7, 9, 10, 11, 12]

# *zip()函数是zip()函数的逆过程，将zip对象变成原先组合前的数据。
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
print(*zip(m, n))
# ([1, 2, 3], [1, 1, 1]) ([4, 5, 6], [2, 2, 3]) ([7, 8, 9], [3, 3, 3])
m2, n2 = zip(*zip(m, n))
m == list(m2) and n == list(n2)
# True

''' 68. __import__() '''
