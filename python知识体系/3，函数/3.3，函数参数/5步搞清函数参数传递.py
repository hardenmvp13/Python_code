'''
1  .Python里面对函数参数传递分以下几种：
位置参数
默认参数  #在函数运行前参数就被赋了值
关键字参数 #通过变量名字进行匹配，而不是通过位置
可变长度参数
1)任意多个非关键字可变长参数(元组)
2)任意多个关键字变量参数(字典)
'''
'''
1.1 位置参数
python中最普通的函数使用是这种带位置参数的函数，
这跟我们其他语言的普通的函数是一样的，所有参数在传递的时候按照位置来传递,列如:
'''


def function1(time, tall):
    print(time, tall)


function1(10, 180)
# 10 180

'''
1.2.默认参数
    一般我们调用函数的时候都会传入值，但是懒人有的时候，希望我输入了值就用我的，
    我懒的时候不输入了python也能给我一个默认值，这就用到了默认参数的特性,看个例子吧:
'''


def printMessage(message, times=2):
    print(message * times)


printMessage('Hi Python:')  # 没有输入times的值
# Hi Python:Hi Python:
# 看我们很懒，没有输入times的值，python就会自动用times的默认值2,是不是很爽
# 其实这个特性对我们开发产品的时候非常有帮助，有的时候一个函数有很多参数，
# 但是为了给用户比较好的体验和方便，我们给函数提供了一套默认的参数，这样对用户来说很爽。
# 当用户慢慢的对你的产品熟悉了，他希望自己调整参数，就可以直接去设参数.
# 其实跟照相机里面的自动模式和手调模式一个道理.

'''
3.关键字参数
    在调用函数的时候，我们希望传递的参数不是僵硬的通过位置来传递，
    能够有一定的灵活性，能通过变量名进行匹配.
'''


def fun2(a, b=10, c=20):
    print(a, b, c)


fun2(6, 7)  # 没有关键词就用默认的位置传递
fun2(25, c=35)
fun2(b=99, c=2, a=10)
# 6 7 20
# 25 10 35
# 10 99 2

'''
4.任意多个位置参数的函数

python有两种方式声明可变参数，我们先说第一种:
在printScore函数中，我们做一小丢丢的改动，我们在参数values前面加*,变成(msg,*values),表示只有第一个参数的msg是调用者必须要指定的，
该参数后面，可以跟任意数量的位置参数(主要是任意数量，当然包含懒人专用的省略不写拉)

def printScore(msg,*values):
	if not values:
		print msg
	else:
		values_str=', '.join(str(x)for x in values)
		print('{},{}'.format(msg,values_str))


printScore('My scores are')
>>My scores are

是不是很爽，刚才说任意数量，我们加多个参数试试看：
printScore('My scores are',100,90,80)
>>My scores are,100, 90, 80
一下把100,90,80都打印出来呢，是怎么做到的，是因为python会自动把*操作符后面的形参变成元组传给函数.
'''
'''
5.任意多个关键字形式的参数
python有两种方式声明可变参数，我们接着说第二种:如何能接受任意数量的关键字参数，是用**双星号操作符来表示
'''


def printlog(msg, **the_rest):
    if not the_rest:
        print(msg)
    else:
        for key, value in the_rest.items():
            print('{},{}={}'.format(msg, key, value))


printlog('abc', a='1.0', c='99.9')
# abc,a=1.0
# abc,c=99.9


'''
最后，用例子总结一下
'''
# 综合例子:
# 好最后拿一个综合例子结尾:(包含了关键字参数，默认参数，可变任意数量参数)


def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords.get(key)
    return count


print(total(10, 1, 2, 3, apple=50, orange=100))
# 166
