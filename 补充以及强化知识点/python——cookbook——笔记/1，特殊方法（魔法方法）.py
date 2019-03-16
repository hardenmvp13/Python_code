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
# 此时运行程序，并没有返回值
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


class A3:
    count = 0

    def addcount(self):
        self.__class__.count += 1


# a3 = A3()
# a3.addcount()
# print(a3.count)
# # 1
# b3 = A3()
# b3.addcount()
# print(b3.count)
# 2
'''
从运行结果可以看出，虽然a和b是两个不同的A类的实例对象，但采用了__class__之后，分别调用两个对象的addcount方法之后，
获取到的对象的count属性却是在不断累加的(这是重点)，
此时self.__class__.count不再是单纯的某个对象私有的属性，而是类的所有实例对象的共有属性,它相当于self.A.count。
'''
# 若将self.__class__.count += 1变为self.count += 1,此时__class__的效果就十分明显了。


class A3:
    count = 0

    def addcount(self):
        self.count += 1


# a3 = A3()
# a3.addcount()
# print(a3.count)
# # 1
# b3 = A3()
# b3.addcount()
# print(b3.count)
# 1          （注意这里count的值还是1，因为这时候count分别是a3，b3对象的私有属性）

'''
4、__str__：在将对象转换成字符串str(对象)测试的时候，打印对象的信息，__str__方法必须要return一个字符串类型的返回值，
            作为对实例对象的字符串描述，__str__实际上是被print函数默认调用的（重点）
            当要print（实例对象）时，默认调用__str__方法，将其字符串描述返回。
            如果不是要用str()函数转换，当你打印一个类的时候，那么print首先调用的就是类里面的定义的__str__。
'''
class A4:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return ("我是A4类的实例对象a4，我的名字叫做：%s"%self.name)
# a4 = A4("哈登")
# print(a4)
# 我是A4类的实例对象a4，我的名字叫做：哈登
# print(A4)
# <class '__main__.A4'>

# 把上诉代码放到控制台上面，就可以看出，直接敲a的话，__str__方法是不会被调用的，而print(a)的时候，__str__就被调用了。例如下图所示：
# print(a4)
# 我是A4类的实例对象a4，我的名字叫做：哈登
# a4
# <A4 object at 0x0000016A49F71B38>

#也可以这样子显示
# print(str(a4))     使用str方法
# 我是A4类的实例对象a4，我的名字叫做：哈登
# 其实__str__相当于是str()方法,str是针对于让人更好理解的字符串格式化

'''
5,__repr__ 如果说__str__体现的是一种可读性，是给用户看的，
           那么__repr__方法体现的则是一种准确性，是给开发人员看的，
           它对应的是repr()函数，重构__repr__方法后，在控制台直接敲出实例对象的名称，就可以按照__repr__中return的值显示了。
'''
class A4:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return ("我是A4类的实例对象a4，我的名字叫做：%s"%self.name)
    def __repr__(self):
        return ("哈哈哈哈，我是A4类的实例对象a4")
# a4 = A4("哈登")
# a4
# 哈哈哈哈，我是A4类的实例对象a4
# print(a4)
# 我是A4类的实例对象a4，我的名字叫做：哈登

# 当然也可以这样子操作
# print(repr(a4))
# 哈哈哈哈，我是A4类的实例对象a4
'''
打印操作会首先尝试__str__和str内置函数(print运行的内部等价形式)，它通常应该返回一个友好的显示。
__repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示。
当我们想所有环境下都统一显示的话，可以重构__repr__方法；当我们想在不同环境下支持不同的显示，例如终端用户显示使用__str__，
而程序员在开发期间则使用底层的__repr__来显示，实际上__str__只是覆盖了__repr__以得到更友好的用户显示。
'''

'''
6,__del__: 对象在程序运行结束之后进行垃圾回收的时候调用这个方法，来释放资源。此时，此方法是被自动调用的。
           除非有特殊要求，一般不要重写。在关闭数据库连接对象的时候，可以在这里，释放资源。
'''
class NewClass(object):
    num_count = 0   #所有的实例都共享这个变量，也就是不单独为每一个变量分配空间
    def __init__(self, name):
        self.name = name
        NewClass.num_count += 1
        print(self.name,NewClass.num_count)
    def __del__(self):
        NewClass.num_count -= 1
        print("del：", self.name, NewClass.num_count)
    def test(self):
        print("aa")
# newclass1 = NewClass("harden")
# newclass2 = NewClass("james")
# newclass3 = NewClass("kobe")
# print("over")
# harden 1
# james 2
# kobe 3
# over
# del： harden 2
# del： james 1
# del： kobe 0
'''
可以看出在程序运行结束之后，__del__默认被调用了三次，分别对实例对象newclass1,newclass2,newclass3进行垃圾回收，因为此时创建的实例已经没有对象再指向它了。
总而言之，__del__魔法方法是在对象没有变量再引用，其引用计数减为0，进行垃圾回收的时候自动调用的。
'''

'''
7、__getattribute__：属性访问拦截器，在访问实例属性时自动调用。在python中，类的属性和方法都理解为属性，
                        且均可以通过__getattribute__获取。当获取属性时，相当于对属性进行重写，直接return object.__getattribute__(self, *args, **kwargs)或者根据判断return所需要的重写值，
                        如果需要获取某个方法的返回值时，则需要在函数后面加上一个()即可。如果不加的话，返回的是函数引用地址。
'''
class Test(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = "cpp"
    def __getattribute__(self, item):
        if item == "subject1":
            return "redirect python"
        else:
            return object.__getattribute__(self, item)
# s = Test("python")
# print(s.subject1)
# print(s.subject2)
# redirect python
# cpp
'''
在创建实例对象s并对其初始化的时候，subject1的值设置为‘python’，subject2的值设置为‘cpp’，
在访问s的subject1属性时，因为Test类对object类中的__getattribute__方法进行了重写，
所以在调用此方法时，首先对要访问的属性做一个拦截和判断，此时__getattribute__方法中的参数obj对应的是要访问的属性，
若要访问subject1属性，则对该属性进行重写，返回了一个不同的字符串，
我们可以看到，在初始化时，subject1 的值为‘python’，而在访问subject1这个属性时，返回的值是'redirect python'，而在访问subject2时，则调用其父类中的__getattribute__方法，返回正常的subject2属性的值。
当然，在访问类的方法属性时，也可以通过重写__getattribute__的方法对其进行重写。
'''

'''
8、__bases__：获取指定类的所有父类构成元素，使用方法为类名.__bases__
'''
class A:
    pass
class B(A):
    pass
class C:
    pass
class D(B, C):
    pass
# print(D.__bases__)
# (<class '__main__.B'>, <class '__main__.C'>)

'''
9、__mro__：显示指定类的所有继承脉络和继承顺序，假如这个指定的类不具有某些方法和属性，
            但与其有血统关系的类中具有这些属性和方法，则在访问这个类本身不具有的这些方法和属性时，
            会按照__mro__显示出来的顺序一层一层向后查找，直到找到为止。
'''
class A:
    pass
class B(A):
    pass
class C:
    pass
class D(B, C):
    pass
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)

'''
10、__call__:具有__call__魔法方法的对象可以使用XXX()的形式被调用，比如说类的实例对象
'''
class Dog(object):
    def __init__(self):
        print("__init__正在被调用————")
# laowang = Dog()
# laowang()
# TypeError: 'Dog' object is not callable   出错

#进行修改
class Dog(object):
    def __init__(self):
        print("__init__正在被调用————")
    def __call__(self):
        print("__cal__正在被调用————")
# laowang = Dog()
# laowang()
# __init__正在被调用————
# __cal__正在被调用————

'''
11、魔法属性：__slots__:可以限制实例对象的属性和方法，但是对类不起作用。
'''

'''
12、__all__:将一个py文件作为模块导入时，其中if __name__ == "main"以上的类、方法、函数等都能被导入，
            但某些方法可能只是用来做测试用的，不希望也不建议被导入，可以用__all__=['函数名或方法名']的方式限制一下哪些函数或方法可以被导入，
            即[]中的函数名或方法名可以被导入。但是需要强调的是，__all__魔法方法只针对通过 from xx import *这种导入方式有效。
'''