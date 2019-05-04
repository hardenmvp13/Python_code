'''
断言:
    被用作你接下来的程序执行，如果后面程序依赖于前面的程序，后面的程序有很重要，
    就是后面的程序执行肯定不能出错，所以在执行之前要做检查工作。
'''
'''1、断言assert'''
class C(object):
    age = 100
    def __init__(self):
        self.name = "AAAAA"

# 没有出现错误的
c_obj = C()
assert c_obj.name == "AAAAA"  # 断言
assert c_obj.age == 100
print("没有错误继续...")
# 没有错误继续...

# 出现错误的就是
# assert c_obj.age == 1
# AssertionError
