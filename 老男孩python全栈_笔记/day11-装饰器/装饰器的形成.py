#装饰器形成的过程
#装饰器的作用
#原则：开放封闭原则
# 装饰器的固定模式

#不懂技术
import time
# time.time() #从1970年到现在经历了多少秒
print(time.time()) # 获取当前时间
time.sleep(3) #作用是让程序睡眠3分钟
print('3秒钟以后开始输出结果')

def fun_1():
    start_time = time.time()
    print('火箭总冠军')
    time.sleep(1)
    end_time = time.time()
    print(end_time-start_time)

fun_1()

# 改进
# 计算函数的执行时间
def time_couter(fun):
    start_time = time.time()
    fun()
    end_time = time.time()
    return end_time-start_time

def fun_2():
    time.sleep(1)
    print("哈登mvp")

time_couter(fun_2)
# 但是这样子还是不完善，因为要执行fun_2，还是要调用time_couter函数
# 因此要继续完善
# time_couter(fun_2())

