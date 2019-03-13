'''
1.未使用的最小的ID

你需要管理大量数据，使用零基础和非负ID来使每个数据项都是唯一的！
因此，需要一个方法来计算下一个新数据项返回最小的未使用ID...
注意：给定的已使用ID数组可能未排序。出于测试原因，可能存在重复的ID，但你无需查找或删除它们！
def next_id(arr):
    #your code here

测试用例：
Test.assert_equals(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
Test.assert_equals(next_id([5,4,3,2,1]), 0)
Test.assert_equals(next_id([0,1,2,3,5]), 4)
Test.assert_equals(next_id([0,0,0,0,0,0]), 1)
Test.assert_equals(next_id([]), 0)
'''
#1，自己的代码
def next_id(arr):
    arr = sorted(arr)
    res = 0
    if len(arr) == 0:
        print(0)
    else:
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == 1 or arr[i+1] - arr[i] == 0:
                res = arr[i+1] + 1
            else:
                break
        print(res)
if __name__ == "__main__":
    next_id([0,1,2,3,4,5,6,7,8,9,10])
    next_id([5,4,3,2,1])
    next_id([0,1,2,3,5])
    next_id([0,0,0,0,0,0])
    next_id([])

#2，别人的代码（使用成员运算符 in）
def next_id2(arr):
    i = 0
    while i in arr:
        i +=1
    return i
if __name__ == "__main__":
    print(next_id2([0,1,2,3,4,5,6,7,8,9,10]))
    print(next_id2([]))

#3,别人的代码（使用内置函数 enumerate ：返回一个可以枚举的对象）

def next_id3(arr):
    if len(arr) ==0:
        return 0
    else:
        arr_new = sorted(set(arr))
        if arr_new[len(arr_new) - 1] == len(arr_new) - 1:
            return len(arr_new)
        else:
            for i,value in enumerate(arr_new):
                if i == value:
                    continue
                else:
                    return i

if __name__ == "__main__":
    print(next_id3([0,1,2,3,4,5,6,7,8,9,10]))
    print(next_id3([]))
