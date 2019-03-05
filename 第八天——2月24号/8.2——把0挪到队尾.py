'''
2.把0挪到队尾

编写一个算法，该算法采用数组并将所有零移动到最后，保留其他元素的顺序。
例如：
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

测试用例：
Test.describe("Basic tests")
Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
Test.assert_equals(move_zeros(["a","b"]),["a","b"])
Test.assert_equals(move_zeros(["a"]),["a"])
Test.assert_equals(move_zeros([0,0]),[0,0])
Test.assert_equals(move_zeros([0]),[0])
Test.assert_equals(move_zeros([False]),[False])
Test.assert_equals(move_zeros([]),[])
'''

def move_zeros(lists):
    new_list = []
    zeros_list = []
    for i in lists:
        if i == 0 and len(str(i)) <5:
            zeros_list.append(0)
        else:
            new_list.append(i)
    return new_list + zeros_list

if __name__ == "__main__":
    print(move_zeros([False,1,0,1,2,0,1,3,"a"]))
    print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
    print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
