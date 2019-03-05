'''
面向过程： 根据业务需要从上到下写代码
面向对象： 将数据与函数绑定在一起，进行封装，这样能够更加快速的开发程序，减少重复代码的重写过程
'''
'''
##############  1,self  ################
    self在定义时需要定义，但是在调用时会自动传入。(谁调用就传谁)
    self的名字并不是规定死的，但是最好还是按照约定是用self
    self总是指调用时的类的实例（对象），而不是类。
'''
class Cat:
    '''定义了一个Cat类'''
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("猫喝水")
    def introduction(self):
        #print("%s今年已经%d岁了"%(tom.name,tom.age))
        print("%s今年已经%d岁了"%(self.name, self.age))

tom = Cat()  #创建一个对象，叫做tom
#调用tom指向对象中的两个方法
tom.drink()
tom.eat()
#给tom指向的对象中添加2个属性
tom.name = "汤姆"
tom.age = 18
tom.introduction()   #self的意义：相当于 tom.introduction(tom )
'''
猫喝水
猫吃鱼
汤姆今年已经18岁了
'''

lanmao = Cat()  #创建一个对象，叫做蓝猫
lanmao.name = "蓝猫"
lanmao.age = 58
lanmao.introduction()
'''
汤姆今年已经18岁了

##明显不是我们想要的，我们需要的答案是“蓝猫今年已经58岁了”
##问题就是出在print("%s今年已经%d岁了"%(tom.name,tom.age))，我们要把tom.name,tom.age修改成self.name,self.age就可以了
'''
print("\n")
#修改以后的输出
'''
蓝猫今年已经58岁了
'''

'''
魔法方法
##############  2,__init__  ################
    初始化对象
'''

class Cat:
    '''定义了一个Cat类'''
    #初始化对象
    def __init__(self):
        print("一开始就要运行我")
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("猫喝水")
    def introduction(self):
        #print("%s今年已经%d岁了"%(tom.name,tom.age))
        print("%s今年已经%d岁了"%(self.name, self.age))

tom = Cat()  #
tom.drink()
tom.eat()
tom.name = "汤姆"
tom.age = 18
tom.introduction()
'''
一开始就要运行我
猫喝水
猫吃鱼
汤姆今年已经18岁了
'''
lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 58
lanmao.introduction()
'''
一开始就要运行我
蓝猫今年已经58岁了
'''

#接下来进行改进,得到升级版本，也就是通用的写法
class Cat:
    '''定义了一个Cat类'''
    #初始化对象，添加默认的属性
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
        #print("一开始就要运行我")
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("猫喝水")
    def introduction(self):
        #print("%s今年已经%d岁了"%(tom.name,tom.age))
        print("%s今年已经%d岁了"%(self.name, self.age))

tom = Cat("汤姆",18)
tom.drink()
tom.eat()
#tom.name = "汤姆"
#tom.age = 18
tom.introduction()
'''
猫喝水
猫吃鱼
汤姆今年已经18岁了
'''

lanmao = Cat("蓝猫",58)
#lanmao.name = "蓝猫"
#lanmao.age = 58
lanmao.introduction()
'''
蓝猫今年已经58岁了
'''

'''
魔法方法
################## 3，__str__  ################
__str__()函数就可以帮助我们打印对象中具体的属性值，或者你想得到的东西
'''
class Cat:
    '''定义了一个Cat类'''
    #初始化对象，添加默认的属性
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
        #print("一开始就要运行我")
    def __str__(self):
        return "%s今年已经%d岁了"%(self.name, self.age)
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("猫喝水")
    #def introduction(self):
        #print("%s今年已经%d岁了"%(tom.name,tom.age))
        #print("%s今年已经%d岁了"%(self.name, self.age))

tom = Cat("汤姆",18)
lanmao = Cat("蓝猫",58)

print(tom)
print(lanmao)
'''
汤姆今年已经18岁了
蓝猫今年已经58岁了
'''