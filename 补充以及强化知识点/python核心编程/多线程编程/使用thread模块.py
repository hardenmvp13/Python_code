'''
使用thread模块
'''
import _thread
from time import sleep,ctime
#睡眠4秒的函数
def loop4():
    print("睡眠4秒的函数开始于(亲，这里要等待4秒哦)：",ctime())
    sleep(4)
    print("睡眠4秒的函数结束于：",ctime())

#睡眠2秒的额函数
def loop2():
    print("睡眠2秒的函数开始于(亲，这里要等待2秒哦)：",ctime())
    sleep(2)
    print("睡眠2秒的函数开始于：",ctime())

def main():
    print("主函数开始的时间：",ctime())
    _thread.start_new_thread(loop2,())
    _thread.start_new_thread(loop4,())
    # sleep(6)
    print("所有函数结束的时间：", ctime())

if __name__ == "__main__":
    main()

# 主函数开始的时间： Sun Mar 10 16:33:16 2019
# 睡眠2秒的函数开始于(亲，这里要等待2秒哦)： Sun Mar 10 16:33:16 2019
# 睡眠4秒的函数开始于(亲，这里要等待4秒哦)： Sun Mar 10 16:33:16 2019
# 睡眠2秒的函数开始于： Sun Mar 10 16:33:18 2019
# 睡眠4秒的函数结束于： Sun Mar 10 16:33:20 2019
# 所有函数结束的时间： Sun Mar 10 16:33:22 2019

'''
如果不加sleep(6),就会得到以下的结果：
'''
# 主函数开始的时间： Sun Mar 10 16:37:18 2019
# 所有函数结束的时间： Sun Mar 10 16:37:18 2019
'''
作用是：这是因为我们如果没有阻止主线程继续执行，他将会继续执行下一条语句，然后显示“所有函数结束”然后退出
而loop4()和loop2()这两个线程就会被直接终止
'''