'''
try except (异常捕获)
    当程序出错了，但是我们又不想让用户看到这个错误，而且我在写程序的时候已经预料到了它可以出现这样的错误，
    出现这样的错误代表着什么，我们可以提前捕获这些个错误
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
# 处理单个异常：
name = [1, 2, 3]
try:
    name[3]  # 不存在3这个下标值
except IndexError as e:   # 抓取 IndexError 这个异常
    print(e) # e是错误的详细信息
# list index out of range



# 处理多个异常：
name = [1, 2, 3]
data = {"a": "b"}
try:
    data["c"]   # 这边已经出现异常KeyError ，所以直接跳出code，跳到KeyError 下去处理
    name[3]
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)

# else作用
# 作用：没有异常，则走else部分的逻辑代码

try:
    print("qigao,handson")    #代码没有异常
except (IndexError,KeyError) as e:
    print(e)
except Exception as e:
    print(e)
else:             #没有异常出错，走else的逻辑代码
    print("没有异常")
# qigao,handson
# 没有异常

# finally
# 作用：不管有没有错误，都会执行finnally中的代码
# 没有异常的情况
try:
    print("qigao,handson")  #没有异常
except (IndexError,KeyError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("不管有没有错，都这行finnally")
# qigao,handson
# 没有异常
# 不管有没有错，都这行finnally

# 出现异常的情况
try:
    data = {"a":"b"}
    data["c"]   # data字典中没有'c'这个key值
except (IndexError,KeyError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("不管有没有错，都这行finnally")

# 'c'
# 不管有没有错，都这行finnally   #出错了也执行了finnally语句