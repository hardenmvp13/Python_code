'''
2.反转字符串

编写一个函数，它接受一个或多个单词的字符串，其中里面含五个或更多字母单词必须要反转。传入的字符串只包含字母和空格。仅当存在多个单词时才会包含空格。

比如:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

测试用例：
test.assert_equals(spin_words("Welcome"), "emocleW")
'''
#倒叙  string[::-1]  以及 reversed()
def spinWords(strings):
    res = []
    for string in strings.split(" "):
        if len(string) >= 5:
            res.append(string[::-1])
        else:
            res.append(string)
    return res
if __name__ == "__main__":
    print(spinWords( "Hey fellow warriors" ))
    print(spinWords("This is a test"))
    print(spinWords("This is another test"))



'''
#自己写的
def spinWords(strings):
    res = []
    for string in strings.split(" "):
        if len(string) > 5:
            for i in range((len(string)-1),-1,-1):
                res.append(i[])
            res.append("")
    return res
if __name__ == "__main__":
    print(spinWords( "Hey fellow warriors" ))

运算结果：
['w', 'o', 'l', 'l', 'e', 'f', '', 's', 'r', 'o', 'i', 'r', 'r', 'a', 'w', '']


'''

