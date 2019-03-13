'''
1.找到大写字母

写一个函数capitals()给你一串字符串，找到里面的大写字母，并返回它们的index.
比如：
capitals('CodEWaRs')输出为 [0,3,4,6]
'''

def capitals(string):
    nums = []
    for str in string:
        if str.isupper():
            nums.append(string.index(str))
    return nums

if __name__ =="__main__":
    print(capitals("CodEWaRs"))