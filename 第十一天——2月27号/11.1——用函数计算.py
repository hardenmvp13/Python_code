'''
1.用函数计算
这次我们想用函数编写计算并得到结果。我们来看看一些例子：
例如：
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
'''
def zero(func= None):
    return func(0) if func else 0
def one(func= None):
    return func(1) if func else 1
def two(func= None):
    return func(2) if func else 2
def three(func= None):
    return func(3) if func else 3
def four(func= None):
    return func(4) if func else 4
def five(func= None):
    return func(5) if func else 5
def six(func= None):
    return func(6) if func else 6
def seven(func= None):
    return func(7) if func else 7
def eight(func= None):
    return func(8) if func else 8
def nine(func= None):
    return func(9) if func else 9
def times(x):
    return lambda y:x*y
def plus(x):
    return lambda y:x+y
def minus(x):
    return lambda y:y-x
def dividedBy(x):
    return lambda y:y//x
if __name__ == '__main__':
    print(seven(times(five())))
    print(four(plus(nine())))
    print(eight(minus(three())))
    print(six(dividedBy(two())))

