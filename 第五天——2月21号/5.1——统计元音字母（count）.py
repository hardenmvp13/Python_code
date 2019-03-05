'''
1.统计元音字母

给一个字符串，统计里面的元音字母！我们给定的元音列表是:[a, e, i, o, u ] ,输入的字符串只会是小写字母或者含有空格。

代码:
def getCount(inputStr):
    num_vowels = 0
    # your code here

    return num_vowels
测试用例：
test.assert_equals(getCount("abracadabra"), 5)
'''
def getCount(inputStr):
    num_vowels = 0
    vowels = [ "a", "e", "i", "o", "u"]
    for i in vowels:
        num_vowels += inputStr.count(i)
    return num_vowels
if __name__ == "__main__":
    print(getCount("abracadabra"))