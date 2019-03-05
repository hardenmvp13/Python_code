'''
###################  正则表达式  #############
'''
'''
  1,正则表达式元字符和语法

符号	                            说明	                                                            实例
.	                            表示任意字符                                           	  'abc'  >>>'a.c'   >>>结果为:'abc' 
^	                           表示字符串开头。	                                          'abc'  >>>'^abc'  >>>结果为:'abc'
$	                             表示字符串结尾。	                                      'abc'  >>>'abc$'  >>>结果为:'abc'

*, +, ?	      '*'表示匹配前一个字符重复 0 次到无限次，                                    'abcccd'  >>>'abc*' >>>结果为:'abccc'
              '+'表示匹配前一个字符重复 1次到无限次，                                     'abcccd' >>>'abc+'  >>>结果为:'abccc'
              '?'表示匹配前一个字符重复 0 次到1                                           'abcccd' >>>'abc?'  >>>结果为:'abc'

*?, +?, ??	    前面的*,+,?等都是贪婪匹配，也就是尽可能多匹配，                           'abc'  >>>'abc*?' >>>结果为:'ab'
                后面加?号使其变成惰性匹配即非贪婪匹配	                                  'abc'  >>>'abc??' >>>结果为:'ab'
                                                                                          'abc'  >>>'abc+?' >>>结果为:'abc'
                                                                                          
{m}	                     匹配前一个字符 m 次	                                          'abcccd' >>>'abc{3}d'  >>>结果为:'abcccd'
{m,n}	                 匹配前一个字符 m 到 n 次	                                      'abcccd'  >>> 'abc{2,3}d' >>>结果为:'abcccd'
{m,n}?	       匹配前一个字符 m 到 n 次，并且取尽可能少的情况 	                          'abccc'  >>> 'abc{2,3}?' >>>结果为:'abcc'

\	               对特殊字符进行转义，或者是指定特殊序列	                                   'a.c' >>>'a\.c' >>> 结果为: 'a.c'
[..]           表示一个字符集,所有特殊字符在其都失去特殊意义,                                    'abcd' >>>'a[bc]' >>>结果为:'ab'
                只有： ^  -  ]  \   含有特殊含义	             
|	           或者，只匹配其中一个表达式 ，
            如果|没有被包括在()中，则它的范围是整个正则表达式	                           'abcd' >>>'abc|acd' >>>结果为:'abc'
            
( … )	             被括起来的表达式作为一个分组. 
                findall 在有组的情况下只显示组的内容	                                   'a123d' >>>'a(123)d' >>>结果为:'123'
(?#...)     	注释，忽略括号内的内容  特殊构建不作为分组	                               'abc123' >>>'abc(?#fasd)123' >>>结果为:'abc123'
(?= … )	   表达式’…’之前的字符串，特殊构建不作为分组	                              在字符串’ pythonretest ’中 (?=test) 
                                                                                                会匹配’ pythonre ’
(?!...)	      后面不跟表达式’…’的字符串，特殊构建不作为分组                         如果’ pythonre ’后面不是字符串’ test ’，
                                                                                        那么 (?!test) 会匹配’ pythonre ’
(?<= … )	   跟在表达式’…’后面的字符串符合括号之后的正则表达式，
                            特殊构建不作为分组	                                          正则表达式’ (?<=abc)def ’
                                                                                            会在’ abcdef ’中匹配’ def ’

（?:）	        取消优先打印分组的内容	                                                   'abc' >>>'(?:a)(b)' >>>结果为'[b]'

?P<>	       指定Key                                                                   'abc' >>>'(?P<n1>a)>>>
                                                                                             结果为:groupdict{n1:a}

'''
'''
  2,正则表达式特殊序列
        特殊表达式序列	           说明
        \A	              只在字符串开头进行匹配。
        \b	              匹配位于开头或者结尾的空字符串
        \B                匹配不位于开头或者结尾的空字符串
        \d	              匹配任意十进制数，相当于 [0-9]
        \D	              匹配任意非数字字符，相当于 [^0-9]
        \s	              匹配任意空白字符，相当于 [ \t\n\r\f\v]
        \S	              匹配任意非空白字符，相当于 [^ \t\n\r\f\v]
        \w	              匹配任意数字和字母，相当于 [a-zA-Z0-9_]
        \W	              匹配任意非数字和字母的字符，相当于 [^a-zA-Z0-9_]
        \Z	              只在字符串结尾进行匹配

  上面提到贪婪匹配和非贪婪匹配请看例子：

        import re
        #贪婪
        ret_greed= re.findall(r'a(\d+)','a23b') 
        print(ret_greed)
        #非贪婪
        ret_no_greed= re.findall(r'a(\d+?)','a23b')
        print(ret_no_greed)
        
        >>['23']
        >>['2']
'''
'''
###########################  re模块  #########################  
          正则表达式使用反斜杠” \ “来代表特殊形式或用作转义字符，这里跟Python的语法冲突，
          因此，Python用” \\ “表示正则表达式中的” \ “，因为正则表达式中如果要匹配” \ “，
          需要用\来转义，变成” \ “，而Python语法中又需要对字符串中每一个\进行转义，所以就变成了” \\ “。
        
          上面的写法是不是觉得很麻烦，为了使正则表达式具有更好的可读性，Python特别设计了原始字符串(raw string)，
          需要提醒你的是，在写文件路径的时候就不要使用raw string了，这里存在陷阱。raw string就是用’r’作为字符串的前缀，
          如 r”\n”：表示两个字符”\”和”n”，而不是换行符了。Python中写正则表达式时推荐使用这种形式。

  1、 re.findall(pattern, string[, flags]):   方法能够以列表的形式返回能匹配的子串。先看简单的例子：
        
            import re
            a = 'one1two2three3four4'
            ret = re.findall(r'(\d+)',a)
            print(ret)
            ['1', '2', '3', '4']
            从上面的例子可以看出返回的值是个列表，并且返回字符串中所有匹配的字符串。

  2、re.finditer(pattern, string[, flags])   搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。 请看例子：
        
            import re
             
            p = re.compile(r'\d+')
            for m in p.finditer('one1two2three3four4'):
                print m.group(),
            
            ### output ###
            # 1 2 3 4　
        
  3、re.match和re.search    Python提供了两种不同的原始操作：match和search。match是从字符串的起点开始做匹配，
                               而search（perl默认）是从字符串做任意匹配。看个例子:
                               
            match（）函数是在string的开始位置匹配，如果不匹配，则返回None
            search()会扫描整个string查找匹配；也就是说match（）只有在0位置匹配成功的话才有返回，
            例如：
            print(re.match(‘super’, ‘superstition’).span())   会返回(0, 5)
            而print(re.match(‘super’, ‘insuperable’))   则返回None
              search()会扫描整个字符串并返回第一个成功的匹配
            例如：print(re.search(‘super’, ‘superstition’).span())返回(0, 5)
            print(re.search(‘super’, ‘insuperable’).span())返回(2, 7)

            import re
            ret_match= re.match("c","abcde");     #从字符串开头匹配，匹配到返回match的对象，匹配不到返回None
            if(ret_match):
                print("ret_match:"+ret_match.group());
            else:
                print("ret_match:None");
            ret_search = re.search("c","abcde"); #扫描整个字符串返回第一个匹配到的元素并结束，匹配不到返回None
            if(ret_search):
                print("ret_search:"+ret_search.group());
    
            ret_match:None
            ret_search:c      
        
        re.match对象拥有以下方法：
        
                        import re
                a = "123abc456"
                ret_match= re.match("a","abcde");
                print(ret_match.group())  #返回返回被 RE 匹配的字符串
                print(ret_match.start())  #返回匹配开始的位置
                print(ret_match.end())    #返回匹配结束的位置
                print(ret_match.span())   #返回一个元组包含匹配 (开始,结束) 的位置
                其中group()方法可以指定组号，如果组号不存在则返回indexError异常看如下例子：
                
        import re
        a = "123abc456"
        re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体默认返回group(0)
        re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
        re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
        re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456

  4，re.sub和re.subn   两种方法都是用来替换匹配成功的字串,值得一提的时，sub不仅仅可以是字符串，也可以是函数。subn函数返回元组，看下面例子:

            import  re
            #sub
            ret_sub = re.sub(r'(one|two|three)','ok','one word two words three words') #ok word ok words ok words
            #subn
            import  re
            ret_subn = re.subn(r'(one|two|three)','ok','one word two words three words') #('ok word ok words ok words', 3) 3,表示替换的次数

  5、re.split(pattern, string, maxsplit=0)   通过正则表达式将字符串分离。如果用括号将正则表达式括起来，
                                              那么匹配的字符串也会被列入到list中返回。
                                              maxsplit是分离的次数，maxsplit=1分离一次，默认为0，不限制次数。看一下例子：

            import re
            ret = re.split('\d+','one1two2three3four4') #匹配到1的时候结果为'one'和'two2three3four4'，匹配到2的时候结果为'one', 'two'和'three3four4', 所以结果为：
            ####output####
            ['one', 'two', 'three', 'four', '']
        
  6，re.compile(strPattern[, flag])    这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。
                                        第二个参数flag是匹配模式，取值可以使用按位或运算符’|’表示同时生效，
                                        比如re.I | re.M。另外，你也可以在regex字符串中指定模式，
                                        比如re.compile(‘pattern’, re.I | re.M)与re.compile(‘(?im)pattern’)是等价的。
                                        可选值有：

            re.I(IGNORECASE): 忽略大小写（括号内是完整写法，下同）
            re.M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
            re.S(DOTALL): 点任意匹配模式，改变'.'的行为
            re.L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
            re.U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
            re.X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
            请看例子：
            
            import re
            text = "JGood is a handsome boy, he is cool, clever, and so on..."
            regex = re.compile(r'\w*oo\w*')
            print(regex.findall(text))
            
            ['JGood', 'cool']
'''