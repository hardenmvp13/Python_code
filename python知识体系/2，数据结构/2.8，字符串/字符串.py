'''
##############一，创建空白字符串##############
'''
string = ' '

'''
##############二,访问字符串中的值#############
'''
var1 = 'Hello World!'
var2 = "Runoob"
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
# var1[0]:  H
# var2[1:5]:  unoo

'''
###############三，字符串更新#################
截取字符串的一部分并与其他字段拼接
'''
var1 = 'Hello World!'
print("已更新字符串 : ", var1[:6] + 'Runoob!')
# 已更新字符串 :  Hello Runoob!

'''
#############四,Python转义字符#################
    转义字符	    描述
    \(在行尾时)	  续行符
    \\	         反斜杠符号
    \'	           单引号
    \"	           双引号
    \a	             响铃
    \b	        退格(Backspace)
    \e	             转义
    \000	         空
    \n	            换行
    \v         	纵向制表符
    \t	      横向制表符
    \r        	   回车
    \f	           换页
'''

'''
################五,Python字符串运算符####################
    操作符	       描述	                                             实例
    +	       字符串连接	                                     a + b 输出结果： HelloPython
    *	     重复输出字符串               	                     a*2 输出结果：HelloHello
    []	    通过索引获取字符串中字符	                           a[1] 输出结果 e
    [ : ]	截取字符串中的一部分，遵循左闭右开原则，
            str[0,2] 是不包含第 3 个字符的。	                 a[1:4] 输出结果 ell
    in	    成员运算符 - 如果字符串中包含给定的字符返回 True	      'H' in a 输出结果 True
    not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	  'M' not in a 输出结果 True
    %	         格式字符串	                                            详细见6
'''

'''
##################六,Python字符串格式化#########################
    Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
    但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
    在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
    python字符串格式化符号:
     符号	      描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
'''
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
# 我叫小明今年10岁!

'''
#############################七,Python 的字符串内建函数##############################
'''
'''
1 ,capitalize()     将字符串的第一个字符转换为大写
'''
str = "this is string example from runoob....wow!!!"
print("str.capitalize() : ", str.capitalize())
# str.capitalize() :  This is string example from runoob....wow!!!

'''
2,center(width, fillchar)  返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
                           width -- 字符串的总宽度。
                           fillchar -- 填充字符。
'''
str = "[www.runoob.com]"
print("str.center(40, '*') : ", str.center(40, '*'))
# str.center(40, '*') :  ************[www.runoob.com]************

'''
3,count(str, beg= 0,end=len(string))
            返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
            sub -- 搜索的子字符串
            start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
            end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
'''
str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))
sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))
#  str.count('o') :  3
#  str.count('run', 0, 10) :  1

'''
4,bytes.decode(encoding="utf-8", errors="strict")
          Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，
          这个 bytes 对象可以由 str.encode() 来编码返回。
'''
str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))
# 菜鸟教程
# UTF-8 编码： b'\xe8\x8f\x9c\xe9\xb8\x9f\xe6\x95\x99\xe7\xa8\x8b'
# GBK 编码：   b'\xb2\xcb\xc4\xf1\xbd\xcc\xb3\xcc'
# UTF-8 解码： 菜鸟教程
# GBK 解码：   菜鸟教程

'''
5,encode(encoding='UTF-8',errors='strict')
          以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，
          除非 errors 指定的是'ignore'或者'replace'
  例子同上
'''
'''
6，endswith(suffix, beg=0, end=len(string))
           用法：str.endswith(suffix[, start[, end]])
           用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
           可选参数"start"与"end"为检索字符串的开始与结束位置。
'''
Str = 'Runoob example....wow!!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 20))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))
# True
# True
# False
# False

'''
7，expandtabs(tabsize=8)  把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。(略)
'''

'''
  8,find(str, beg=0 end=len(string))
         检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，
         返回值：如果包含返回开始的索引值，否则返回-1
             str -- 指定检索的字符串
             beg -- 开始索引，默认为0。
             end -- 结束索引，默认为字符串的长度。
'''
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.find(str2))
print(str1.find(str2, 5))
print(str1.find(str2, 10))
# 7
# 7
# -1

'''
9,index(str, beg=0, end=len(string))  跟find()方法一样，只不过如果str不在字符串中会报一个异常.
'''
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.index(str2))
print(str1.index(str2, 5))
print(str1.index(str2, 10))
# 7
# 7
#   File "D:/python练习代码/知识星球/Knowledge-planet/补充以及强化知识点/字符串.py", line 217, in <module>
#       print (str1.index(str2, 10))
#     ValueError: substring not found

'''
10，isalnum()  检测字符串是否由字母和数字组成,是返回 True,否则返回 False
'''
str = "runoob2016"  # 字符串没有空格
print(str.isalnum())
str = "www.runoob.com"
print(str.isalnum())
# True
# False

'''
11, isalpha()   检测字符串是否只由字母组成  # alpha：阿尔法
'''

'''
12, isdigit()   检测字符串是否只由数字组成  # digit：数字，注意是只由
'''

'''
13, islower()   检测字符串是否由小写字母组成, 是则返回 True，否则返回 False
'''

'''
14, isnumeric()  如果字符串中只包含数字字符，则返回 True，否则返回 False，这种方法是只针对unicode对象
'''

'''
15, isspace()    如果字符串中只包含空白，则返回 True，否则返回 False.
'''

'''
16, istitle()   检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
'''
str = "This Is String Example...Wow!!!"
print(str.istitle())
str = "This is string example....wow!!!"
print(str.istitle())
# True
# False

'''
17，isupper()  如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，
             则返回 True，否则返回 False
'''

'''
18, join(sequence)   以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
                  sequence - - 要连接的元素序列。
'''
seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
print("-".join(seq))
print("".join(seq))
# r-u-n-o-o-b
# runoob

'''
19,len(string)    返回字符串长度
'''

'''
20,ljust(width[, fillchar])  返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
                           如果指定的长度小于原字符串的长度则返回原字符串。
                           width -- 指定字符串长度。
                           fillchar -- 填充字符，默认为空格。
'''
str = "Runoob example....wow!!!"
print(str.ljust(50, '*'))
# Runoob example....wow!!!**************************

'''
21，lower()  转换字符串中所有大写字符为小写.
'''
str = "Runoob EXAMPLE....WOW!!!"
print(str.lower())
# runoob example....wow!!!

'''
22，lstrip()  语法：str.lstrip([chars])
            截掉字符串左边的空格或指定字符。
            chars --指定截取的字符。
'''
str = "     this is string example....wow!!!     "
print(str.lstrip())
str = "88888888this is string example....wow!!!8888888"
print(str.lstrip('8'))
# this is string example....wow!!!
# this is string example....wow!!!8888888

'''
23，maketrans()  语法：str.maketrans(intab, outtab)
              创建字符映射的转换表，对于接受两个参数的最简单的调用方式。
              两个字符串的长度必须相同，为一一对应的关系。
              intab -- 字符串中要替代的字符组成的字符串。
              outtab -- 相应的映射字符的字符串。
              Python3.4 已经没有 string.maketrans() 了，
              取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans() 。
'''
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print(str.translate(trantab))
# >> th3s 3s str3ng 2x1mpl2....w4w!!!

'''
24，max(str)   返回字符串 str 中最大的字母。
25，min(str)   返回字符串 str 中最小的字母。
'''
'''
26,replace(old, new [, max])
                             把字符串中的 old（旧字符串） 替换成 new(新字符串)，
                             如果指定第三个参数max，则替换不超过 max 次。
                               old -- 将被替换的子字符串。
                               new -- 新字符串，用于替换old子字符串。
                               max -- 可选字符串, 替换不超过 max 次
'''
str = "www.w3cschool.cc"
print("菜鸟教程旧地址：", str)
print("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
str = "this is string example....wow!!!"
print(str.replace("is", "was", 3))
# 菜鸟教程旧地址： www.w3cschool.cc
# 菜鸟教程新地址： www.runoob.com
# thwas was string example....wow!!!

# 下面四个与是上面的左边起相对应，从右边开始
'''
27，rfind(str, beg=0,end=len(string))    类似于 find()函数，不过是从右边开始查找.
28,rindex( str, beg=0, end=len(string))  类似于 index()，不过是从右边开始.
29,rjust(width,[, fillchar])             返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
30,rstrip()                              删除字符串字符串末尾的空格.
'''

'''
31,split(str="", num=string.count(str))
                  指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串
                        str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
                        num -- 分割次数。默认为 -1, 即分隔所有。
'''
str = "this is string example....wow!!!"
print(str.split())       # 以空格为分隔符
print(str.split('i', 1))   # 以 i 为分隔符
print(str.split('w'))     # 以 w 为分隔符
# ['this', 'is', 'string', 'example....wow!!!']
# ['th', 's is string example....wow!!!']
# ['this is string example....', 'o', '!!!']

'''
32，splitlines([keepends])
       按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
       如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
       keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
'''
'ab c\n\nde fg\rkl\r\n'.splitlines()
# ['ab c', '', 'de fg', 'kl']
'ab c\n\nde fg\rkl\r\n'.splitlines(True)
# ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

'''
33，startswith(substr, beg=0,end=len(string))
            检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。
            如果beg 和 end 指定值，则在指定范围内检查。
                    str -- 检测的字符串。
                    substr -- 指定的子字符串。
                    strbeg -- 可选参数用于设置字符串检测的起始位置。
                    strend -- 可选参数用于设置字符串检测的结束位置。
'''
str = "this is string example....wow!!!"
print(str.startswith('this'))   # 字符串是否以 this 开头
print(str.startswith('string', 8))  # 从第八个字符开始的字符串是否以 string 开头
print(str.startswith('this', 2, 4))  # 从第2个字符开始到第四个字符结束的字符串是否以 this 开头
# True
# True
# False

'''
34,strip([chars])
               用于移除字符串头尾指定的字符（默认为空格）或字符序列。
               在字符串上执行 lstrip()和 rstrip()
               注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
'''
str = "*****this is **string** example....wow!!!*****"
print(str.strip('*'))  # 指定字符串 *
# this is **string** example....wow!!!

'''
35，swapcase()   将字符串中大写转换为小写，小写转换为大写
'''
str = "this is string example....wow!!!"
print(str.swapcase())
str = "This Is String Example....WOW!!!"
print(str.swapcase())
# THIS IS STRING EXAMPLE....WOW!!!
# tHIS iS sTRING eXAMPLE....wow!!!

'''
36，title()    返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
'''
str = "this is string example from runoob....wow!!!"
print(str.title())
# This Is String Example From Runoob....Wow!!!

'''
37，translate(table, deletechars="")
       根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
           table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
           deletechars -- 字符串中要过滤的字符列表。
'''
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表
str = "this is string example....wow!!!"
print(str.translate(trantab))
# th3s 3s str3ng 2x1mpl2....w4w!!!

# 以下实例演示如何过滤掉的字符 o：
# 制作翻译表
bytes_tabtrans = bytes.maketrans(
    b'abcdefghijklmnopqrstuvwxyz',
    b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))
# b'RUNB'

'''
38,upper()          转换字符串中的小写字母为大写
'''
'ab'.upper()
# 'AB'

'''
39，zfill (width)   返回长度为 width 的字符串，原字符串右对齐，前面填充0
'''

'''
40,isdecimal()     检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''
