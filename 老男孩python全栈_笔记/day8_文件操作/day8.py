'''
1，文件操作
    例如：哈登.txt
        （1），文件路径：F:\哈登.txt
        （2），编码方式：utf-8，gbk
        （3），操作方式：只读，只写，追加，读写，写读
        以什么编码方式存储的文件，就用什么编码方式打开进行操作
    只读：r
'''
# 绝对路径
file = open('F:\哈登.txt', mode='r', encoding='utf-8') #mode：模式
file_read = file.read()
print(file_read)
file.close()
# mvp