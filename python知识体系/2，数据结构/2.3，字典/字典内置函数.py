'''
#############修改字典##########
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

dict['Age']:  8
dict['School']:  菜鸟教程

###########删除字典元素##########
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典

'''

'''
###################  字典内置函数以及方法  ######################
'''

'''
#######内置函数#######

  1，len(dict)  计算字典元素个数，即键的总数。
	
        >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
        >>> len(dict)
            3

  2，str(dict)  输出字典，以可打印的字符串表示。	
  
        >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
        >>> str(dict)
        "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"

  3，type(variable)     返回输入的变量类型，如果变量是字典就返回字典类型。	
  
        >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
        >>> type(dict)
        <class 'dict'>
'''

'''
############方法###########

  1,clear()  删除字典内所有元素
            dict.clear()
            参数无，返回值无

        dict = {'Name': 'Zara', 'Age': 7}
        print ("字典长度 : %d" %  len(dict))
        dict.clear()
        print ("字典删除后长度 : %d" %  len(dict))
        
        >>字典长度 : 2
        >>字典删除后长度 : 0

  2,copy()  返回一个字典的浅复制
            dict.copy()
            参数无，返回值无
            
        dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
        dict2 = dict1.copy()
        print("新复制的字典为 : ", dict2)
    
        >>新复制的字典为 :  {'Age': 7, 'Name': 'Runoob', 'Class': 'First'}

  3,fromkeys(seq[, value])  用于创建一个新字典
                            dict.fromkeys(seq[, value])
                            seq -- 字典键值列表。
                            value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
                            创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
        
        seq = ('name', 'age', 'sex')
        dict = dict.fromkeys(seq)
        print("新的字典为 : %s" % str(dict))
        dict = dict.fromkeys(seq, 10)
        print("新的字典为 : %s" % str(dict))

        >>新的字典为 : {'age': None, 'name': None, 'sex': None}
        >>新的字典为 : {'age': 10, 'name': 10, 'sex': 10}
        
  4,get(key, default=None)  返回指定键的值，如果值不在字典中返回default值
                            dict.get(key, default=None)
                            key -- 字典中要查找的键。
                            default -- 如果指定键的值不存在时，返回该默认值值。

        dict = {'Name': 'Runoob', 'Age': 27}
        print ("Age 值为 : %s" %  dict.get('Age'))
        print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))
        
        >>Age 值为 : 27
        >>Sex 值为 : NA

  5，key in dict   如果键在字典dict里返回true，否则返回false

  6,items()       以列表返回可遍历的(键, 值) 元组数组
                  dict.items()
                  参数无，返回可遍历的(键, 值) 元组数组。

        dict = {'Name': 'Runoob', 'Age': 7}
        print ("Value : %s" %  dict.items())
        
        >>Value : dict_items([('Age', 7), ('Name', 'Runoob')])

  7,keys()  返回一个迭代器，可以使用 list() 来转换为列表
            dict.keys()
            参数无
  
        >>> dict = {'Name': 'Runoob', 'Age': 7}
        >>> dict.keys()
        dict_keys(['Name', 'Age'])

  8,setdefault(key, default=None)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
                                    dict.setdefault(key, default=None)
                                    key -- 查找的键值。
                                    default -- 键不存在时，设置的默认键值。

        dict = {'Name': 'Runoob', 'Age': 7}
        print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))
        print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
        print ("新字典为：", dict)
        
        >>Age 键的值为 : 7
        >>Sex 键的值为 : None
        >>新字典为： {'Age': 7, 'Name': 'Runoob', 'Sex': None}

  9, update(dict2)   把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
                     dict.update(dict2)
                     dict2 -- 添加到指定字典dict里的字典。

        dict = {'Name': 'Runoob', 'Age': 7}
        dict2 = {'Sex': 'female'}
        dict.update(dict2)
        print("更新字典 dict : ", dict)
        
        >>更新字典 dict :  {'Name': 'Runoob', 'Age': 7, 'Sex': 'female'}

  10,values()   返回一个迭代器，可以使用 list() 来转换为列表
                dict.values()
                参数无
  
        dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
        print ("字典所有值为 : ",  list(dict.values()))
        
        >>字典所有值为 :  ['female', 'Zara', 7]

  11,pop(key[,default])  删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
                         pop(key[,default])
                           key: 要删除的键值
                           default: 如果没有 key，返回 default 值
                           返回被删除的值。
                           
        >>> site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
        >>> pop_obj=site.pop('name')
        >>> print(pop_obj)
        菜鸟教程
        
  12,popitem()    随机返回并删除字典中的一对键和值(一般删除末尾对)。
                  popitem()
                  参数无

        site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
        pop_obj=site.popitem()
        print(pop_obj)
        print(site)
        
        >>('url', 'www.runoob.com')
        >>{'name': '菜鸟教程', 'alexa': 10000}

'''
