'''
################三元表达式#################
为真时的结果 if 判断条件 else 为假时的结果（注意，没有冒号）
'''

x = 2
y = 3
if x>y:
    print(x)
else:
    print(y)

#应用三元表达式
print(x) if x>y else print(y)
#输出:3


'''
###################列表解析（列表推导式）############################
'''
#普通方式
s='hello'
l=[]
for i in s:
    res=i.upper()    #upper()   大写
    l.append(res)    #append() 方法用于在列表末尾添加新的对象。
print(l)

#列表推导式
s='hello'
res = [i.upper() for i in s]
print(res)

'''
输出结果：['H', 'E', 'L', 'L', 'O']
'''


#普通方式
l=[1,31,73,84,57,22]
l_new=[]
for i in l:
    if i > 50:
        l_new.append(i)
print(l_new)

#列表推导式
l=[1,31,73,84,57,22]
res = [i for i in l if i>50]
print(res)

'''
输出结果：[73, 84, 57]
'''

# 普通方式
l = []
for i in range(10):
    l.append(i)
print(l)

# 列表解析方式
res = [i for i in range(10)]
print(res)

'''
输出结果为：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# 普通方式
l = [1, 2, 3, 4]
l_new = []
for i in l:
    res = i ** 2
    l_new.append(res)
print(l_new)

# 列表解析方式
res = [i ** 2 for i in l]
print(res)

'''
输出结果为：[1, 4, 9, 16]
'''

#应用
l=[1,31,73,84,57,22]
#两个判断条件
print([i for i in l if i > 20 and i < 50])

'''
输出结果：[31, 22]
'''