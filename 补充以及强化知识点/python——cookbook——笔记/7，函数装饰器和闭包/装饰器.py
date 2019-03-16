'''
函数装饰器：用于在源码中“标记”函数，以某种方式增强函数的行为
'''
'''
1，装饰器基础知识
   装饰器：是可调用的对象，其参数是另一个函数（被装饰的函数），装饰器可能会处理被装饰的函数，然后把它们返回，或者是将其替换成另一个函数或者可调用对象
'''
def deco(func):
    def inner():
        print("running inner()")
    return inner
@deco
def target():
    print("running target()")

# target()
# running inner()
# print(target)
# <function deco.<locals>.inner at 0x00000216D83D88C8>
'''
上述代码解释：
（1）deco函数返回inner函数对象
（2）使用deco装饰target
（3）调用被装饰的target其实会运行inner
（4）审查对象，发现target现在是inner的引用
引用：数据的在内存中的地址就是数据的引用。如果两个变量为同一个引用，那么这两个变量对应的数据一定相同；
　　  如果两个变量对应的数据相同，引用不一定相同。通过id(数据）可以查看数据对应的地址，修改变量的值，其实是在修改变量的引用。
'''
'''
综上所述：装饰器有两大特性：（1）能够把装饰的函数替换成其他函数
                            （2）装饰器在加载模块时立即执行
'''

'''
2,python 何时执行装饰器
    装饰器的一大关键属性是：它们在装饰器在加载模块时立即执行
'''
#以下是registration.py
registry = []
def register(func):
    print("running register:(%s)" % func)  #显示被装饰的函数
    registry.append(func)
    return func
@register #f1被@register装饰
def f1():
    print("running f1()")

@register #f2被@register装饰
def f2():
    print("running f2()")

def f3():
    print("running f3()")

def main():
    print("running main()")
    print("registry->", registry)
    f1()
    f2()
    f3()

# if __name__ == '__main__':
#     main()
#如果直接运行（也就是作为脚本运行），结果如下：
# running register:(<function f1 at 0x000001CD744C8AE8>)
# running register:(<function f2 at 0x000001CD744C8A60>)
# running main()
# registry-> [<function f1 at 0x000001CD744C8AE8>, <function f2 at 0x000001CD744C8A60>]
# running f1()
# running f2()
# running f3()

# 如果是导入模板（registration.py）运行，不作为脚本运行，输出如下：
# import registration.py
# running register:(<function f1 at 0x000001CD744C8AE8>)
# running register:(<function f2 at 0x000001CD744C8A60>)
# 此时再查看registry,得到的输出函数如下：
# registration.registey
# [<function f1 at 0x000001CD744C8AE8>, <function f2 at 0x000001CD744C8A60>]
'''
上述例子主要是为了强调：
函数装饰器在导入模板的时候立即运行，而被装饰的函数（f1，f2）只有在明确调用的时候运行
这就是导入时和运行时的不同
'''

'''
3,使用装饰器进行改进“策略”模式
'''
#promos中的值使用promotion装饰器进行填充
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    '''积分为1000或者以上的顾客提供5%的折扣'''
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

'''
4,变量作用域规则
'''
def f1(a):
    print(a)
    print(b)
# f1(3)
#这时候就会报错
#NameError: name 'b' is not defined

# 如果换成这种形式，也会报错
b = 6
def f2(a):
    print(a)
    print(b)
    b = 9
# f2(3)
#UnboundLocalError: local variable 'b' referenced before assignment

#这时候就要global函数出场
b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 9
f3(3)
# 3
# 6

from dis import dis
dis(f1)  #比较字节码   暂时搞不懂

'''
5,闭包
经常和匿名函数搞混，
闭包指的是：延伸了作用域的函数，其中包含函数定义体中引用的'''
