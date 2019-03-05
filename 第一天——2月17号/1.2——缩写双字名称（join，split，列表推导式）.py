'''
2.缩写双字名称

编写一个函数将名称转换为首字母。这个kata严格地用两个词，它们之间有一个空格。
输出应该是两个大写字母，并用点分隔它们。
它应该如下所示：

    Sam Harris` => `S.H
    Patrick Feeney` => `P.F
'''

def addrevName():
    string = str(input("请输入要提取的名字："))
    print(".".join([i[0] for i in string.split( )]))
addrevName()