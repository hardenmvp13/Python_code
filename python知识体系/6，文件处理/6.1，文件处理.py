'''
open:打开文件，创建一个file对象
    mode的参数有：r：只读模式，如果文件不存在就会报错
                  w：只写模式，如果文件不存在就会创建文件，如果存在就会覆盖
                  a：追加模式（从尾部追加）
                  附加：b：二进制模式     如rb，wb
                        t：文本模式（默认）
                        +：支持读写

对象常用函数：
file.read()      字符串的形式返回所有内容
file.readline()  显示一行内容
file.next()      取下一行
file.readlines() 列表的形式返回所有行的内容
file.writelines()写入字符序列的内容
file.truncate()  文件截取内容
file.flush()     刷新，从数据从缓存区写入文件
file.close()     关闭文件
file.tell()      显示文件指针所在位置
file.seek()      定义文件中的指针位置

'''