'''
1,使用__slots__
'''
# 1.1正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
    pass
# 1.2然后，尝试给实例绑定一个属性：
s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)
# Michael

# 1.3还可以尝试给实例绑定一个方法：
def set_age(self, age): # 定义一个函数作为实例方法
      self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果
# 25
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student() # 创建新的实例
# s2.set_age(25) # 尝试调用方法
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'set_age'

# 1.4 为了给所有实例都绑定方法，可以给class绑定方法：









class Student(object):
    # 获取成绩
    def get_score(self):
        return self._score
    # 设置成绩

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
