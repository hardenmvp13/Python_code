'''

1,判断奇数还是偶数
创建一个函数，它以整数作为参数，对偶数返回“偶数”，对奇数返回“奇数”。

'''

def even_or_odd(number):
    print("%d == even"%number) if number%2 == 0 else print("%d == odd"%number)

if __name__ == "__main__":
    even_or_odd(2)
    even_or_odd(0)
    even_or_odd(7)
    even_or_odd(1)
    even_or_odd(-1)


