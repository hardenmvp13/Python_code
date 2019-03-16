'''
函数装饰器：用于在源码中“标记”函数，以某种方式增强函数的行为
'''
'''
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
