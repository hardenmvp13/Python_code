'''
魔法方法：在Python中，所有以“__”双下划线包起来的方法，都统称为“Magic Method”，中文称『魔术方法』,
          这些魔法方法会让对象持有特殊行为，在进行特定的操作时会自动被调用
          例如类的初始化方法 __init__
'''
'''
1,构造与初始化
__init__：初始化函数，在创建实例对象为其赋值时使用，在__new__之后，__init__必须至少有一个参数self，
          就是这个__new__返回的实例，__init__是在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值。
          然而，当调用 x = SomeClass() 的时候， __init__ 并不是第一个被调用的方法。
          实际上，还有一个叫做__new__ 的方法，两个共同构成了“构造函数”。

__new__: 是用来创建类并返回这个类的实例, 而__init__只是将传入的参数来初始化该实例。
        很多人认为__init__是类的构造函数，其实不太确切，__init__更多的是负责初始化操作，相当于一个项目中的配置文件，
        __new__才是真正的构造函数，创建并返回一个实例对象，如果__new__只调用了一次，就会得到一个对象。
        继承自object的新式类才有__new__这一魔法方法，__new__至少必须要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供，
        __new__必须要有返回值，返回实例化出来的实例（很重要）,这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例，
        若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的，即使是父类的实例也不行。
        __new__是唯一在实例创建之前执行的方法，一般用在定义元类时使用。
        创建对象的步骤：
        a、首先调用__new__得到一个对象
        b、调用__init__为对象添加属性
        c、将对象赋值给变量

在对象生命周期调用结束时，__del__ 方法会被调用，可以将__del__理解为“构析函数”。
'''
# 首先来熟悉最基本__init__操作：


class Dog:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
# erha = Dog("颜色是白色","物种是哈士奇")
#此时运行程序，并没有返回值
# print(type(erha))
# <class '__main__.Dog'>
# print(erha.color,erha.brand)
# 颜色是白色 物种是哈士奇

# 下面来看一个结合__init__和__new__两个魔法方法的例子：
class A(object):
    pass
class B(A):
    def __init__(self):
        print("__init__被调用了")
    def __new__(cls):
        print("__new__被调用了")
        print('id(cls):', id(cls))
        return object.__new__(A)
# b = B()
# __new__被调用了
# id(cls): 1443760786360
# print(b)
# <__main__.A object at 0x0000015028AF7A20>
# print(type(b))
# <class '__main__.A'>         类型所继承的基类（也就是A类）
# print(id(A))
# 1443760776920
# print(id(B))
# 1443760786360
'''
从运行结果可以看出：__new__中的参数cls，和B中的id是相同的，表明__new__中默认的参数cls就是B类本身，
                    而在return时，并没有正确返回当前类cls的实例，而是返回了其父类A的实例，因此__init__这一魔法方法并没有被调用，
                    此时__new__虽然是写在B类中的，但其创建并返回的是一个A类的实例对象。
'''

# 现在把return中的参数A变为cls，再来看一下运行结果：
class A(object):
    pass
class B(A):
    def __init__(self):
        print("__init__被调用了")
    def __new__(cls):
        print("__new__被调用了")
        print('id(cls):', id(cls))
        return object.__new__(cls)
# b = B()
# __new__被调用了
# id(cls): 1845486187000
# __init__被调用了
# print(b)
# <__main__.B object at 0x000001ADB1717B70>
# print(type(b))
# <class '__main__.B'>
# print(id(A))
# 1845486186056
# print(id(B))
# 1845486187000
'''
可以看出，当__new__正确返回其当前类cls的实例对象时，__init__被调用了，此时创建并返回的是一个B类的实例对象。
'''

'''3、__class__：获得已知对象的类 ( 对象.__class__)。'''