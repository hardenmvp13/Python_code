'''
2.拼接字符

根据下面的表达式设计一个函数:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

'''


def zccum(s):
    # 使用列表推导式
    s_new = "-".join([i.upper() + i * s.find(i) for i in s])
    print(s_new)


if __name__ == '__main__':
    zccum("abcd")





# length = len(s)
# s_new = ""
# s_new = s.
# # s_upper = s.upper()
# # print(s_upper)
# # for i in range(len(s_upper)):
# #     s_upper = s_upper[:i+1] + s_upper[i+i] + s_upper[i+1:len(s_upper)]
# #     print(s_upper)
