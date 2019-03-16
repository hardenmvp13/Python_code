'''
python的几个内置装饰器：@staticmethod、@classmethod和@property

@staticmethod: 类静态方法  与实例化方法的区别就是没有self参数，并且可以在类不进行实例化的情况下调用
@classmethod:  类方法      与实例化方法的区别就是接受的第一个参数不是self（类实例的指针），而是cls（当前类的具体类型）
@property：    属性方法    讲一个类方法转化成一个类的属性，只读属性

'''
class TestClass(object):
    name = "玩具"
    def __init__(self, name):
        self.name = name
    def objPrint(self, xy):
        print("%s 是实例化方法：%s"%(self.name, xy))
    @classmethod
    def classPrint(cls,xy):
        print("%s 是类方法，只能调用类变量： %s"%(cls, xy))
        print("%s 是类方法，只能调用类变量： %s" % (cls.name, xy))
    @staticmethod
    def staticPrint(xy):
        print("静态方法：%s"%xy)
# obj = TestClass("食物")
# obj.objPrint("方便面")
# TestClass.classPrint("火腿肠")
# TestClass.staticPrint("面包")

# 食物 是实例化方法：方便面
# <class '__main__.TestClass'> 是类方法，只能调用类变量： 火腿肠
# 玩具 是类方法，只能调用类变量： 火腿肠
# 静态方法：面包

'''接着来看@property'''
class TestClass1(object):
    def __init__(self, name):
        self.name = name
        self.__food = None
    @property
    def renwu(self):
        print("%s is eating %s:"%(self.name, self.__food))

    @renwu.setter
    def renwu(self, food):
        print("set to food",food)
        self.__food = food

a =  TestClass1("王刚")
a.renwu
a.renwu = "火腿肠"
a.renwu()

# 王刚 is eating None:
# set to food 火腿肠
# 王刚 is eating 火腿肠:

