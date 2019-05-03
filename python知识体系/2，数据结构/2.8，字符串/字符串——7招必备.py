import re
''' 1.字符串的连接和合并 '''
# 相加  +
s1 = "a"
s2 = 'b'
print(s1 + s2)
# ab

# 合并  join
url = ['www', 'laocui', 'online']
print('-'.join(url))
# www-laocui-online

''' 2,字符串的切片和相乘 '''
# 相乘
print("+" * 10)
# ++++++++++

# 切片
# str[1:7],str[-3:0],   str[::]全部

''' 3.字符串的分割 '''
# 普通的分割，用split,split只能做非常简单的分割，而且不支持多个分隔
phone = '400-800-800-1234'
print(phone.split('-'))
# >>['400', '800', '800', '1234']

# 复杂的分割
# r表示不转义,分隔符可以是;或者,或者空格后面跟0个多个额外的空格，然后按照这个模式去分割
line = 'abc df; python, i ,like,   it'
print(re.split(r'[;,s]\s*', line))
#['abc df', 'python', 'i ', 'like', 'it']

''' 4,字符串的开头和结尾的处理 '''
# 比方我们要查一个文件的名字是以什么开头或者什么结尾
filename = 'trace.h'
print(filename.endswith('h'))
# >>True
print(filename.startswith('trace'))
# >>True

''' 5,字符串的查找和匹配 '''
# 一般查找
# 我们可以很方便的在长的字符串里面查找子字符串，会返回子字符串所在位置的索引, 若找不到返回-1
title = 'abc hjaksdhfj jsd python sjkdfksafd'
print(title.find('python'))
# 18

# 复杂的匹配
# 正则
data = '11/27/2019'
print(re.match(r'\d+/\d+/\d+', data))
# <_sre.SRE_Match object; span=(0, 10), match='11/27/2019'>

''' 6.字符串的替换 '''
# 普通的替换 , 用replace就可以
str = "abc python hsajdk"
print(str.replace('python', 'harden'))
# abc harden hsajdk

# 复杂的替换//若要处理复杂的或者多个的替换，需要用到re模块的sub函数
str = 'abc 6566 jshdjf 5656 shfja 8789787897'
print(re.sub(r'\d+', '100', str))
# abc 100 jshdjf 100 shfja 100

''' 7,字符串中去掉一些字符 '''
# 去除空格,  对文本处理的时候比如从文件中读取一行，然后需要去除每一行的两侧的空格，table或者是换行符
line = '  Congratulations, you guessed it.  	 '
print(line.strip())
# >>Congratulations, you guessed it.
# 注意:字符串内部的空格不能去掉，若要去掉需要用re模块

# 复杂的文本清理,可以利用str.translate，
# 先构建一个转换表，table是一个翻译表，表示把't''o'转成大写的'T' 'O',
# 然后在old_str里面去掉'12345',然后剩下的字符串再经过table翻译

# import string
# instr = 'to'
# outstr = 'TO'
# old_str = 'to to myto thk oj  6627522'
# new_str = old_str.translate()
