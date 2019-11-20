'''一，建立单向链表'''
class student:
    def __init__(self):
        # 完成节点类的声明
        self.name = ''
        self.score = 0
        self.next = None

# 建立一个学生节点的单向链表算法
head = student()  #建立链表的头部
head.next = None  #当前没有下一个元素
ptr = head         #设置存取指针的位置
select = 0

while select != 2:
    print('(1)新增，（2）离开=>')
    try:
        select = int(input('请输入一个选项：'))
    except ValueError:
        print("输入错误")
        print("请重新输入\n")
    if select == 1:
        print("哈登mvp")



