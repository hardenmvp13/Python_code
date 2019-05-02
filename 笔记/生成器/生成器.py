'''
生成器不会把结果保存在一个系列中，而是保存生成器的状态，
      在每次进行迭代时才返回一个值，直到遇到StopIteration异常结束
在Python中，这种一边循环一边计算的机制，称为生成器：generator
'''
def frange(start,stop,increment):
    x=start
    while x<stop:
        yield x
        x+=increment
for i in frange(1,10,2):
    print(i)
'''
1
3
5
7
9
'''
#这个函数没有返回值，怎么会能生成一个序列呢，是不是很神奇.对这就是yield的妙用


# 语法
# 生成器表达式： 通列表解析语法，只不过把列表解析的[]换成()
g= (x**2 for x in range(5))
print(g)
# <generator object <genexpr> at 0x0000000002771798>

L=[x**2 for x in range(5)]
print(L)
# >>[0, 1, 4, 9, 16]
# 也就是说：创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator

'''
生成器函数
        函数中只要出现了yield语句就会将其转变成一个生成器函数
        特别之处在于，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
        与普通函数不一样，生成器值会在迭代操作的时候才能运行.yiled可以把函数中断，保存状态和继续执行的能力
'''
def countdown(n):
   print('Starting to count from',n)
   while n>0:
      yield n
      n-=1
   print('done')
c=countdown(3)
print(c)
# <generator object countdown at 0x0000000002821828>
#表示这是一个生成器
'''
# .调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值

比如:
c=countdown(3)
#run the first yield and emit a value
print next(c)
>>
Starting to count from 3
3

#run the next yield
print next(c)
>>
2
#run the next yield
print next(c)
>>
1

#run the next yield
print next(c)
>>
done
    print next(c)
StopIteration
'''
'''
你把yield想象成时间断点,运行一次next就回放一下，看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值

第一次next()是打印了 print 'Starting to count from',n，提取第一次的保存值是3
第二次再运行next()是继续在while里面的断点接着走，所以没有打印print 'Starting to count from',n， 而是直接提取第二次的保存值2
第三次再运行next()是继续在while里面的断点接着走,所以直接输出1
第四次再运行next()的时候，发现yield缓存的武打片慢镜头都已经放完了，所以输出done之后,报了个错StopIteration
'''
'''
3).生成器函数用for循环

for n in countdown(6):
	print(n)
>>
Starting to count from 6
6
5
4
3
2
1
done
正确的方法是使用for循环，因为generator也是可迭代对象

'''