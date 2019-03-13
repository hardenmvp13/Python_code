'''
给定一个数字，写一个函数来输出其反向数字。（例如，给出123答案是321）
数字应该保留他们的标志; 即反转时负数仍应为负数。
比如:
 123 ->  321
-456 -> -654
1000 ->    1
'''

def reverse_number(seq):
    if seq > 0:
        return int(str(seq)[::-1])
    else:
        return -1*(int(str(abs(seq))[::-1]))

if __name__ == "__main__":
    print(reverse_number(123))
    print(reverse_number(-456))
    print(reverse_number(1000))