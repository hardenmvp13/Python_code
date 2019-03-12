'''
引入锁的概念
'''
a = [1, 2, 3]
b = [10, 10, 10]
print(list(map(lambda x, y: x + y, a, b)))

