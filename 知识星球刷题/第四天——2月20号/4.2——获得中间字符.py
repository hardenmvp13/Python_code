'''
2.获得中间字符
你会得到一个字符串,你需要写一个函数返回单词的中间字符。
如果单词的长度为奇数，则返回中间字符。如果单词的长度是偶数，则返回中间2个字符。

例如：
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
测试用例：
Test.assert_equals(get_middle("test"),"es")
Test.assert_equals(get_middle("testing"),"t")
Test.assert_equals(get_middle("middle"),"dd")
Test.assert_equals(get_middle("A"),"A")
Test.assert_equals(get_middle("of"),"of")
'''
#1，自己的代码
#在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 //

def get_middle(string):
    lenght = len(string)
    print(string[int(lenght/2-1):int(lenght/2+1)]) if lenght%2 == 0 else print(string[int(lenght/2)])

if __name__ == "__main__":
    get_middle("test")
    get_middle("testing")
    get_middle("middle")
    get_middle("A")
    get_middle("of")

#2，别人的代码

