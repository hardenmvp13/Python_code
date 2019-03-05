'''
############## 集合内置方法 #############

  1,add() 为集合添加元素
                set.add(elmnt)
                elmnt -- 必需，要添加的元素。

        fruits = {"apple", "banana", "cherry"}
        fruits.add("orange")
        print(fruits)
        >>{'apple', 'banana', 'orange', 'cherry'}

  2,clear()	移除集合中的所有元素
            set.clear()
            参数无，返回值无

  3,copy()	拷贝一个集合
            set.copy()
            参数无，返回值无

  4,difference()	返回多个集合的差集,返回集合的差集，
                    即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
                    set.difference(set)
                    set -- 必需，用于计算差集的集合
                    返回一个新的集合。

        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        z = x.difference(y)
        print(z)
        >>{'cherry', 'banana'}


  5,difference_update()	移除集合中的元素，该元素在指定的集合也存在。
                            用于移除两个集合中都存在的元素。
                            difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，
                            而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
                            set.difference_update(set)
                            set -- 必需，用于计算差集的集合

        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        x.difference_update(y)
        print(x)
        >>{'cherry', 'banana'}

  6,discard()	   删除集合中指定的元素
                    set.discard(value)
                    value -- 必需，要移除的元素

        fruits = {"apple", "banana", "cherry"}
        fruits.discard("banana")
        print(fruits)
        >>{'cherry', 'apple'}

  7,intersection()	返回集合的交集
                        set.intersection(set1, set2 ... etc)
                        set1 -- 必需，要查找相同元素的集合
                        set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
                        返回一个新的集合。

            x = {"apple", "banana", "cherry"}
            y = {"google", "runoob", "apple"}
            z = x.intersection(y)
            print(z)
            >>{'apple'}

  8,intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
                                set.intersection_update(set1, set2 ... etc)
                                set1 -- 必需，要查找相同元素的集合
                                set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开

            x = {"a", "b", "c"}
            y = {"c", "d", "e"}
            z = {"f", "g", "c"}
            x.intersection_update(y, z)
            print(x)
            >>{'c'}

  9,isdisjoint()	  判断两个集合是否包含相同的元素
                      set.isdisjoint(set)
                      set -- 必需，要比较的集合
                      返回布尔值，如果不包含返回 True，否则返回 False。

            x = {"apple", "banana", "cherry"}
            y = {"google", "runoob", "facebook"}
            z = x.isdisjoint(y)
            print(z)
            >>True

  10,issubset()	  判断集合的所有元素是否都包含在指定集合中
                     set.issubset(set)
                     set -- 必需，要比查找的集合
                     返回布尔值，如果都包含返回 True，否则返回 False。

            x = {"a", "b", "c"}
            y = {"f", "e", "d", "c", "b", "a"}
            z = x.issubset(y)
            print(z)
            >>True

  11,issuperset()	用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False

            x = {"f", "e", "d", "c", "b", "a"}
            y = {"a", "b", "c"}
            z = x.issuperset(y)
            print(z)
            >>True

  12,pop()	随机移除元素

  13,remove()	移除指定元素
                    set.remove(item)

            fruits = {"apple", "banana", "cherry"}
            fruits.remove("banana")
            print(fruits)
            >>{'cherry', 'apple'}


  14,symmetric_difference()	返回两个集合中不重复的元素集合。
                                set.symmetric_difference(set)

            x = {"apple", "banana", "cherry"}
            y = {"google", "runoob", "apple"}
            z = x.symmetric_difference(y)
            print(z)
            >>{'google', 'cherry', 'banana', 'runoob'}



  15,symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，
                                        并将另外一个指定集合中不同的元素插入到当前集合中。

            x = {"apple", "banana", "cherry"}
            y = {"google", "runoob", "apple"}
            x.symmetric_difference_update(y)
            print(x)
            >>{'google', 'cherry', 'banana', 'runoob'}



  16,union()	返回两个集合的并集,即包含了所有集合的元素，重复的元素只会出现一次。

            x = {"apple", "banana", "cherry"}
            y = {"google", "runoob", "apple"}
            z = x.union(y)
            print(z)
            >>{'cherry', 'runoob', 'google', 'banana', 'apple'}


  17,update()	给集合添加元素,可以添加新的元素或集合到当前集合中，
                    如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。

            x = {"apple", "banana", "cherry"}
            y = {"google", "runoob", "apple"}
            x.update(y)
            print(x)
            >>{'banana', 'apple', 'google', 'runoob', 'cherry'}

'''