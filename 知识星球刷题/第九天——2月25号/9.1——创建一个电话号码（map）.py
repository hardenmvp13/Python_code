'''
1.创建一个电话号码

编写一个接受10个整数（0到9之间）数组的函数，它以电话号码的形式返回这些数字的字符串。

例如：

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
'''

def create_phone_number1(req):
    print("returns "+"(%d%d%d)"%(req[0],req[1],req[2])+" "+"%d%d%d"%(req[3],req[4],req[5])+ "-" +"%d%d%d%d"%(req[6],req[7],req[8],req[9]))

if __name__ == "__main__":
    create_phone_number1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
