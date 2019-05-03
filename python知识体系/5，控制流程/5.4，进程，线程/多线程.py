'''
因为：进程只能在一个时间干一件事，如果想同时干两件事或多件事，进程就无能为力了
      进程在执行的过程中如果阻塞，整个进程就会挂起将无法执行
所以出现了线程：
    每一个进程中至少有一个线程。能独立运行的基本单位 ——线程（Threads）
多任务可以由多个进程实现，也可以由多个线程实现。
    threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
    run(): 用以表示线程活动的方法。
    start():启动线程活动。
    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
'''
'''一，使用 threading 模块创建线程'''
import threading
import time
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: （当前时间为：%s）" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "线程1——Thread-1", 2)
thread2 = myThread(2, "线程2——Thread-2", 5)
thread3 = myThread(3, "线程3——Thread-3", 8)

# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("退出主线程")
#
# 开始线程：线程1——Thread-1
# 开始线程：线程2——Thread-2
# 开始线程：线程3——Thread-3
# 线程1——Thread-1: （当前时间为：Sat May  4 01:47:44 2019）
# 线程1——Thread-1: （当前时间为：Sat May  4 01:47:46 2019）
# 线程2——Thread-2: （当前时间为：Sat May  4 01:47:47 2019）
# 线程1——Thread-1: （当前时间为：Sat May  4 01:47:48 2019）
# 线程3——Thread-3: （当前时间为：Sat May  4 01:47:50 2019）
# 线程1——Thread-1: （当前时间为：Sat May  4 01:47:50 2019）
# 线程2——Thread-2: （当前时间为：Sat May  4 01:47:52 2019）
# 线程1——Thread-1: （当前时间为：Sat May  4 01:47:52 2019）
# 退出线程：线程1——Thread-1
# 线程2——Thread-2: （当前时间为：Sat May  4 01:47:57 2019）
# 线程3——Thread-3: （当前时间为：Sat May  4 01:47:58 2019）
# 线程2——Thread-2: （当前时间为：Sat May  4 01:48:02 2019）
# 线程3——Thread-3: （当前时间为：Sat May  4 01:48:06 2019）
# 线程2——Thread-2: （当前时间为：Sat May  4 01:48:07 2019）
# 退出线程：线程2——Thread-2
# 线程3——Thread-3: （当前时间为：Sat May  4 01:48:14 2019）
# 线程3——Thread-3: （当前时间为：Sat May  4 01:48:22 2019）
# 退出线程：线程3——Thread-3
# 退出主线程

'''二，线程同步'''
'''
原因：多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
     而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
     因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
解决方式：
    引入锁的概念，由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
'''
import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")

# 开启线程： Thread-1
# 开启线程： Thread-2
# Thread-1: Wed Apr  6 11:52:57 2016
# Thread-1: Wed Apr  6 11:52:58 2016
# Thread-1: Wed Apr  6 11:52:59 2016
# Thread-2: Wed Apr  6 11:53:01 2016
# Thread-2: Wed Apr  6 11:53:03 2016
# Thread-2: Wed Apr  6 11:53:05 2016
# 退出主线程

'''三，线程优先级队列'''
'''
Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
Queue 模块中的常用方法:
    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]])获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''
import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")

# 开启线程：Thread-1
# 开启线程：Thread-2
# 开启线程：Thread-3
# Thread-3 processing One
# Thread-1 processing Two
# Thread-2 processing Three
# Thread-3 processing Four
# Thread-1 processing Five
# 退出线程：Thread-3
# 退出线程：Thread-2
# 退出线程：Thread-1
# 退出主线程