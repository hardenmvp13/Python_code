'''
1.来排个序

你的任务是对给定的字符串进行排序。字符串中的每个单词都包含一个数字。此数字是单词在结果中应具有的位置。

注意：数字可以是1到9.因此1将是第一个单词（不是0）。

如果输入字符串为空，则返回空字符串。输入String中的单词只包含有效的连续数字。

例子:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
import re
def order(strings):
    # 返回被匹配的字符串
    # match（）函数是在string的开始位置匹配，如果不匹配，则返回None
    # search()会扫描整个string查找匹配；也就是说match（）只有在0位置匹配成功的话才有返回，
    sort_strings = sorted(strings.split(), key=lambda strings: re.search(r'\d+?', strings).group())
    return " ".join(sort_strings)

if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2" ))
    print(order(" "))