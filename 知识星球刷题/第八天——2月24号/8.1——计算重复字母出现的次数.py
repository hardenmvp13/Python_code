'''
1.计算重复字母出现的次数

编写一个函数，该函数将返回在输入字符串中出现多次(不同的不区分大小写的)字母字符和数字的计数。
可以假定输入字符串仅包含字母（大写和小写）和数字。

例如:
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(string):
    string = string.lower()
    string_count = 0
    count = []
    for i in set(string):
        if string.count(i) >1:
            count.append(string.count(i))
            string_count +=1
    print("共有%d重复字符"%string_count,count)
if __name__ == "__main__":
    duplicate_count("abcde")
    duplicate_count("aabbcde")
    duplicate_count("aabBcde")
    duplicate_count("indivisibility")
    duplicate_count("Indivisibilities")
    duplicate_count("aA11")
    duplicate_count("ABBA")



