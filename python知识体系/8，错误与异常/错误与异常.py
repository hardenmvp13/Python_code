'''
当python程序检测到错误（语法错误或者是逻辑错误），程序就会终止执行，这时候就出现了异常
'''
'''
常见的异常有：
AssertionError——断言语句失败
AttributeError——对象没有这个属性，试图访问一个对象没有的属性
IoError——输入/输出操作失败，基本是无法打开文件
ImportError——无法引入模块或者是包，基本是路径问题
IndentationError——语法错误，代码没有正确的对齐（缩进问题）
IndexError——下标索引超出序列边界
KeyError——试图访问字典里面不存在的键
KeyboardInterrupt——用户终端执行
NameError——使用一个还没有赋予对象的变量
SyntaxError——python代码逻辑语法出错，不能执行
TypeError——传入对象类型与要求不符合
UnboundlocalError——试图传入一个还没设置的全局变量
ValueError——传入一个不被期望的值，即使类型正确
'''
'''检测和处理异常：'''
# 处理多个
name = [1,2,3]
try:
    name[3]  #不存在3这个下标值
except IndexError as e:   #抓取 IndexError 这个异常
    print(e) #e是错误的详细信息
# list index out of range

name1 = [1,2,3]
print(name1[4])