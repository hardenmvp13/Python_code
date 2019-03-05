'''
Matplotlib 是一个 Python 的 2D绘图库，通过 Matplotlib，开发者可以仅需要几行代码，
便可以生成绘图，直方图，功率谱，条形图，错误图，散点图等。
当然他也是可以画出3D图形的，这时就需要安装更多的扩展。
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

''' 1、一个简单案例来展示画图的基本命令 '''
'''
plt.plot(x,y,format_string,**kwargs) 
            x轴数据，y轴数据，format_string控制曲线的格式字串 
            format_string 由颜色字符，风格字符，和标记字符 
            **kwargs:第二组或更多，(x,y,format_string)
'''
def drawing1():
    x = np.linspace(0,2*np.pi,100) # 设置横轴变量，从0到2*pi，均分为100份
    y = np.sin(x) # 因变量取值
    plt.plot(x,y,'b*',label='aaa') # 'b*'表示蓝色*状线，label是指定义图例
    plt.plot(x*2,y,'r--',label='bbb') # 'r--'表示红色虚线，
    plt.xlabel('this is x') # 设置横轴标签
    plt.ylabel('this is y') # 设置纵轴标签
    plt.title('this is title') # 设置标题
    plt.legend() # 显示上面定义的图例
    plt.show() # 展示图像
# drawing1()

# 1.Figure，
# 图像，matplotlib中整个图像就是一个figure,在figure对象中可以包含一个或者多个Axes对象。
# 而每个Axes对象又拥有自己坐标系统的绘图区域
def drawing2():
    '''画一个二行一列的坐标图，可以用subplots直接生成一个2*1的2个子图，2就是表示这个图像里面有2个坐标图，1表示是1列'''
    fig = plt.figure()
    fig,ax_lst = plt.subplots(2,1)
    plt.show()
# drawing2()

# 生成多个子图
def drawing3():
    for i ,c in enumerate('gbyc'):
        plt.subplot(2,2,i+1,axisbg = c)
    plt.show()
# drawing3()

## 2,Axes 子图
def drawing4():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    x = [1,2,3,4]
    y = [2,3,4,5]
    ax1.plot(x,y,'o',color = 'r')
    ax1.set_title('simple figure')
    plt.show()
drawing4()

## 3,Axis  是每个子图上x轴和y轴上的线，刻度标记，以及刻度标记的注释
## 4,Artist 所有的图里面的元素其实都是artist


''' 用pyplot画一个漂亮的曲线图 '''
def drawing5():
    x= np.arange(0,3,0.1)
    plt.plot(x,x,label = 'linear')
    plt.plot(x,x**3,label='quadratic')
    plt.plot(x,x**2,label='cubic')
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.legend()
    plt.show()
drawing5()