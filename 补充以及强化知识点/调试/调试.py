'''
debug相关功能
F8：step over 单步
遇到断点后，程序停止运行，按F8单步运行。

F7：step into 进入
配合F8使用。单步调试F8时，如果某行调用其他模块的函数，在此行F7，可以进入函数内部，如果是F8则不会进入函数内容，直接单步到下一行。

Alt+shift+F7：step into mycode,
个人理解F8和F7的综合。1、没遇到函数，和F8一样；2、遇到函数会自动进入函数内部，和F8时按F7类似的

shift+F8：跳出
调试过程中，F7进入函数内后，shift+F8跳出函数，会回到进入前调用函数的代码。不是函数地方shift+F8跳出，怎么用没太明白，但最终会执行到结束。

F9：resume program
按翻译是重启程序 ，实际是 下个断点，当打多个断点是，F9会到下一个断点

常用：
F8，F9，其次Alt+shift+F7，或 F7，shift+F8

'''
def sum(x):
    x += 1
    return x

for i in range(10):
    print(i)
    print(sum(i))
    print(sum(i)*10)
