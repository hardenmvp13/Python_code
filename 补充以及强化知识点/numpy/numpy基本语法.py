'''
1、array
'''
import numpy
list_1 = [1, 2, 3, 4]
array_1 = numpy.array(list_1)  # 一维数组
list_2 = [4, 5, 6, 7]
array_2 = numpy.array([list_1, list_2])  # 二维数组

array_2.shape  # 查看数组特征，eg：2行4列
array_2.size  # 查看元素个数, eg:8
array_2.dtype  # 查看数组类型，eg：int64
# 注：numpy.arange(n) #与python中的range区别是前面有个a

s = [2, 3]
a = 3
print(numpy.zeros(s))  # 全0矩阵，s可以为一个数也可以为一个列表，eg：[2,3]表示2*3的二维数组
'''
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
 '''
print(numpy.eye(a))  # 单位矩阵，生成的是浮点数
'''
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
 '''
# 访问数组中元素：
# 一维：array_1[2] 、array_1[1:4]
# 二维：array_2[1][2] 、array_2[1,2] 、array_2[:1,1:4]
# 其中可以根据python中列表的切片来访问数据

'''
2、数组与矩阵运算
'''
'''2.1数组'''
print(numpy.random.randn(10))  # 十个元素的一维数组
'''
[ 1.8181173   0.38727013 -0.35549011 -0.37512919 -1.50123451  0.05836567
 -0.42490392 -0.30897512  0.22426378 -0.95545405]
 '''
print(numpy.random.randint(10, size=20).reshape(4, 5)
      )  # 产生20个10以内的随机整数，后面的reshape是将这些数重新写成一个4*5的二维数组
'''
[[7 0 8 9 4]
 [5 2 2 2 9]
 [8 3 9 0 9]
 [6 1 8 5 9]]
 '''
'''2.2矩阵'''
print(numpy.array([[1, 2, 3], [4, 5, 6]], dtype=int))
'''
[[1 2 3]
 [4 5 6]]
'''
