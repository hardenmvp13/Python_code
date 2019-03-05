'''
2.递归数字总和

写一个函数叫digital_root,给定一个数字，递归遍历数字从个位，十位，百位...以此相加计算总和。则以这种方式继续减少，直到产生一位数字。这仅适用于自然数

比如:
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
'''

#没有用到递归思想
def digital_root(num):
    str_num = list(str(num))
    while True:
        sums = 0
        if len(str_num) >1:
            for i in str_num:
                sums += int(i)
                str_num = str(sums)
        else:
            break
    return int(str_num)

# if __name__ == "__main__":
#     print(digital_root(16))
#     print(digital_root(942))
#     print(digital_root(132189))
#     print(digital_root(493193))

#群主的代码(使用递归)
def digital_root1(num):
    str_num = str(num)
    if len(str_num) ==1:
        return str_num
    else:
        return digital_root1(sum([int(i) for i in str_num]))

if __name__ == "__main__":
    print(digital_root1(16))
    print(digital_root1(942))
    print(digital_root1(132189))
    print(digital_root1(493193))