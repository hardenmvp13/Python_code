'''
进程：对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，
      打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
线程：有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。
      在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
'''
'''
multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
'''
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# Parent process 25572.
# Child process will start.
# Run child process test (24324)...
# Child process end.

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

'''
Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# Parent process 25952.
# Waiting for all subprocesses done...
# Run task 0 (26232)...
# Run task 1 (26224)...
# Run task 2 (26104)...
# Run task 3 (26096)...
# Task 2 runs 0.14 seconds.
# Run task 4 (26104)...
# Task 3 runs 0.60 seconds.
# Task 4 runs 0.50 seconds.
# Task 1 runs 1.04 seconds.
# Task 0 runs 1.51 seconds.
# All subprocesses done.
