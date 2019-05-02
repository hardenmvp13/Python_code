'''
不使用线程
'''
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
    loop4()
    loop2()
    print("所有函数结束的时间：", ctime())

if __name__ == "__main__":
    main()
# 主函数开始的时间： Sun Mar 10 16:19:01 2019
# 睡眠4秒的函数开始于(亲，这里要等待4秒哦)： Sun Mar 10 16:19:01 2019
# 睡眠4秒的函数结束于： Sun Mar 10 16:19:05 2019
# 睡眠2秒的函数开始于： Sun Mar 10 16:19:05 2019
# 睡眠2秒的函数开始于： Sun Mar 10 16:19:07 2019
# 所有函数结束的时间： Sun Mar 10 16:19:07 2019
