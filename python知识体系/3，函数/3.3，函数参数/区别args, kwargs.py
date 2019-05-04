'''
*args和**kwargs主要用于函数定义。你可以将不定数量的参数传递给某个函数。
*args     是用来发送一个非键值对的可变数量的参数列表给一个函数.
            将参数打包成tuple给函数体调用
**kwargs  将不定长度的键值对作为参数传递给一个函数。如果你想要在一个函数里处理带名字的参数，你应该使用**kwargs。
            打包关键字参数成dict给函数体调用
'''
def function1(x, y, *args):
    print(x, y, args)

function1(1, 2, 3, 4, 5, 6, 7)
# 1 2 (3, 4, 5, 6, 7)

def function2(x, y, **kwargs):
    print(x, y, kwargs)
# function(1, 2, 3, 4, 5, 6, 7)
# TypeError: function() takes 2 positional arguments but 7 were given
function2(1, 2, a= 3, b= 4, c= 5, d= 6, e= 7)
# 1 2 {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7}

def function3(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
function3(1, 2, 3, 4, 5, 6, 7, a= 3, b= 4, c= 5, d= 6, e= 7)
# 1 2 (3, 4, 5, 6, 7) {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7}