'''
1，文件操作
    例如：哈登.txt
        （1），文件路径：F:\哈登.txt
        （2），编码方式：utf-8，gbk
        （3），操作方式：只读，只写，追加，读写，写读
        以什么编码方式存储的文件，就用什么编码方式打开进行操作

'''
###只读：r ，rb
# 绝对路径
file = open('F:\哈登.txt', mode='r', encoding='utf-8') #mode：模式
file_read = file.read()
print(file_read)
file.close()
# mvp

###只写： w  如果没有此文件，就会创建文件，再写
#            如果已经存在文件，就先将源文件清空，再写
file = open('F:\log1.txt', mode='wb') #mode：模式
# file_read = file.read()
file.write('哈登mvp，这是重新写入的方法'.encode('gbk'))
# print(file_read)
file.close()
