'''
#################一,创建列表####################
    创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
        list = []
'''

'''
###############二,访问列表中的值################
    使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符

        list1 = ['Google', 'Runoob', 1997, 2000];
        list2 = [1, 2, 3, 4, 5, 6, 7];
        print("list1[0]: ", list1[0])
        print("list2[1:5]: ", list2[1:5])
        
        >>list1[0]:  Google
        >>list2[1:5]:  [2, 3, 4, 5]
'''

'''
###################三,更新列表#####################
    可以对列表的数据项进行修改或更新，也可以使用append()方法来添加列表项.

        list = ['Google', 'Runoob', 1997, 2000]
        print("第三个元素为 : ", list[2])
        list[2] = 2001
        print("更新后的第三个元素为 : ", list[2])
        
        >>第三个元素为 :  1997
        >>更新后的第三个元素为 :  2001
'''

'''
#####################四,删除列表元素###################
    可以使用 del 语句来删除列表的的元素

        list = ['Google', 'Runoob', 1997, 2000]
        
        print("原始列表 : ", list)
        del list[2]
        print("删除第三个元素 : ", list)
        
        >>原始列表 :  ['Google', 'Runoob', 1997, 2000]
        >>删除第三个元素 :  ['Google', 'Runoob', 2000]
'''

'''
######################五,Python列表脚本操作符###########
    列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表

        Python 表达式	              结果	                          描述
        [1, 2, 3] + [4, 5, 6]	  [1, 2, 3, 4, 5, 6]   	              组合
        ['Hi!'] * 4	         ['Hi!', 'Hi!', 'Hi!', 'Hi!']	          重复
'''

"""
###################六,Python列表截取与拼接##################
    截取
        >>>L=['Google', 'Runoob', 'Taobao']
        >>> L[2]
        'Taobao'
        >>> L[-2]
        'Runoob'
        >>> L[1:]
        ['Runoob', 'Taobao']
    拼接：
        >>>squares = [1, 4, 9, 16, 25]
        >>> squares += [36, 49, 64, 81, 100]
        >>> squares
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        
        python 中的[:-1]和[::-1]
        a='python'
        b=a[::-1]
        print(b) #nohtyp
        c=a[::-2]
        print(c) #nhy
        #从后往前数的话，最后一个位置为-1
        d=a[:-1]  #从位置0到位置-1之前的数
        print(d)  #pytho
        e=a[:-2]  #从位置0到位置-2之前的数
        print(e)  #pyth

"""

'''
####################七,嵌套列表##################
    使用嵌套列表即在列表里创建其它列表
        >>>a = ['a', 'b', 'c']
        >>> n = [1, 2, 3]
        >>> x = [a, n]
        >>> x
        [['a', 'b', 'c'], [1, 2, 3]]
        >>> x[0]
        ['a', 'b', 'c']
        >>> x[0][1]
        'b'
'''

'''
####################八，列表函数&方法########################
'''
'''
############8.1函数#############
    1	len(list)  列表元素个数
    2	max(list)  返回列表元素最大值
    3	min(list)  返回列表元素最小值
    4	list(seq)  将元组转换为列表
'''

'''
############8.2方法##############

  1,list.append(obj)   在列表末尾添加新的对象
                        obj -- 添加到列表末尾的对象。
                        该方法无返回值，但是会修改原来的列表。

        list1 = ['Google', 'Runoob', 'Taobao']
        list1.append('Baidu')
        print ("更新后的列表 : ", list1)
        
        >>更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']

  2,list.count(obj)     统计某个元素在列表中出现的次数
                            obj -- 列表中统计的对象。
                            返回元素在列表中出现的次数。

        aList = [123, 'Google', 'Runoob', 'Taobao', 123];
        
        print ("123 元素个数 : ", aList.count(123))
        print ("Runoob 元素个数 : ", aList.count('Runoob'))
        
        >>123 元素个数 :  2
        >>Runoob 元素个数 :  1

  3,list.extend(seq)   在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
                         seq -- 元素列表，可以是列表、元组、集合、字典，
                                若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
                         该方法没有返回值，但会在已存在的列表中添加新的列表内容。

        list1 = ['Google', 'Runoob', 'Taobao']
        list2=list(range(5)) # 创建 0-4 的列表
        list1.extend(list2)  # 扩展列表
        print ("扩展后的列表：", list1)
        
        >>扩展后的列表： ['Google', 'Runoob', 'Taobao', 0, 1, 2, 3, 4]

  4,list.index(obj)  从列表中找出某个值第一个匹配项的索引位置
                       obj -- 查找的对象。
                       返回查找对象的索引位置，如果没有找到对象则抛出异常。

        list1 = ['Google', 'Runoob', 'Taobao']
        print ('Runoob 索引值为', list1.index('Runoob'))
        print ('Taobao 索引值为', list1.index('Taobao'))
        
        >>Runoob 索引值为 1
        >>Taobao 索引值为 2

  5,list.insert(index, obj)  将对象插入列表
                               index -- 对象obj需要插入的索引位置。
                               obj -- 要插入列表中的对象。
                               该方法没有返回值，但会在列表指定位置插入对象。

        list1 = ['Google', 'Runoob', 'Taobao']
        list1.insert(1, 'Baidu')
        print ('列表插入元素后为 : ', list1)
        
        >>列表插入元素后为 :  ['Google', 'Baidu', 'Runoob', 'Taobao']

  6,list.pop([index=-1])      移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
                                 index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，
                                          默认为 index=-1，删除最后一个列表值。

        list1 = ['Google', 'Runoob', 'Taobao']
        list1.pop()
        print ("列表现在为 : ", list1)
        list1.pop(1)
        print ("列表现在为 : ", list1)
        
        >>列表现在为 :  ['Google', 'Runoob']
        >>列表现在为 :  ['Google']

   7,list.remove(obj)  移除列表中某个值的第一个匹配项
                        obj -- 列表中要移除的对象。
                        该方法没有返回值但是会移除列表中的某个值的第一个匹配项。

        list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
        list1.remove('Taobao')
        print ("列表现在为 : ", list1)
        list1.remove('Baidu')
        print ("列表现在为 : ", list1)
        
        >>列表现在为 :  ['Google', 'Runoob', 'Baidu']
        >>列表现在为 :  ['Google', 'Runoob']

  8,list.reverse()   反向列表中元素

        list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
        list1.reverse()
        print ("列表反转后: ", list1)
        
        >>列表反转后:  ['Baidu', 'Taobao', 'Runoob', 'Google']

  9,list.sort(cmp=None, key=None, reverse=False)   对原列表进行排序
                                                    key -- 主要是用来进行比较的元素，只有一个参数，
                                                           具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
                                                    reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

        l = [[2, 2, 3], [1, 4, 5], [5, 4, 9]]
        l.sort(lambda x: x[0])  ##按照第一个元素进行排序
        print(l)
        
        >>[[1, 4, 5], [2, 2, 3], [5, 4, 9]]
        #匿名函数的x，表示的是l列表中的每一个成员元素 ,x[0] :表示列表里面列表的第一个成员元素

  10,list.clear()     清空列表

        list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
        list1.clear()
        print ("列表清空后 : ", list1)
        
        >>列表清空后 :  []

  11,list.copy()      复制列表

        list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
        list2 = list1.copy()
        print ("list2 列表: ", list2)
        
        >>list2 列表:  ['Google', 'Runoob', 'Taobao', 'Baidu']
'''