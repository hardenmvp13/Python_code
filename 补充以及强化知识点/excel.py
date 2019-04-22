import xlwt

#设置表格样式
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

#写Excel
def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('学生',cell_overwrite_ok=True)
    row0 = ["姓名","年龄","出生日期","爱好"]
    colum0 = ["张三","李四","恋习Python","小明","小红","无名"]
    #写第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    #写第一列
    for i in range(0,len(colum0)):
        sheet1.write(i+1,0,colum0[i],set_style('Times New Roman',220,True))

    sheet1.write(1,3,'2006/12/12')
    sheet1.write_merge(6,6,1,3,'未知')#合并行单元格
    sheet1.write_merge(1,2,3,3,'打游戏')#合并列单元格
    sheet1.write_merge(4,5,3,3,'打篮球')

    f.save('test.xls')

if __name__ == '__main__':
    write_excel()
'''
结果图：

640?wx_fmt=png

在此，对write_merge()的用法稍作解释，如上述：sheet1.write_merge(1,2,3,3,'打游戏')，即在四列合并第2,3列，合并后的单元格内容为"合计"，并设置了style。其中，里面所有的参数都是以0开始计算的。

640?wx_fmt=png

Python读Excel——xlrd

Python读取Excel表格，相比xlwt来说，xlrd提供的接口比较多，但过程也有几个比较麻烦的问题，比如读取日期、读合并单元格内容。

640?wx_fmt=jpeg

下面先看看基本的操作：

640?wx_fmt=png

（图表数据）

整体思路为，打开文件，选定表格，读取行列内容，读取表格内数据

详细代码如下：

import xlrd
from datetime import date,datetime

file = 'test3.xlsx'

def read_excel():

    wb = xlrd.open_workbook(filename=file)#打开文件
    print(wb.sheet_names())#获取所有表格名字

    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    sheet2 = wb.sheet_by_name('年级')#通过名字获取表格
    print(sheet1,sheet2)
    print(sheet1.name,sheet1.nrows,sheet1.ncols)

    rows = sheet1.row_values(2)#获取行内容
    cols = sheet1.col_values(3)#获取列内容
    print(rows)
    print(cols)

    print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    print(sheet1.cell_value(1,0))
    print(sheet1.row(1)[0].value)
运行结果如下：

640?wx_fmt=png

那么问题来了，上面的运行结果中红框框中的字段明明是出生日期，可显示的确实浮点数；同时合并单元格里面应该是有内容的，结果不能为空。

别急，我们来一一解决这两个问题：

1.Python读取Excel中单元格内容为日期的方式

Python读取Excel中单元格的内容返回的有5种类型，即上面例子中的ctype：

ctype :  0 empty，1 string，2 number， 3 date，4 boolean，5 error

即date的ctype=3，这时需要使用xlrd的xldate_as_tuple来处理为date格式，先判断表格的ctype=3时xldate才能开始操作。

详细代码如下：

import xlrd
from datetime import date,datetime

print(sheet1.cell(1,2).ctype)
date_value = xlrd.xldate_as_tuple(sheet1.cell_value(1,2),wb.datemode)
print(date_value)
print(date(*date_value[:3]))
print(date(*date_value[:3]).strftime('%Y/%m/%d'))
运行结果如下：

640?wx_fmt=png

2.获取合并单元格的内容

在操作之前，先介绍一下merged_cells()用法，merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),其中[row,row_range)包括row,不包括row_range,col也是一样，即(1, 3, 4, 5)的含义是：第1到2行（不包括3）合并，(7, 8, 2, 5)的含义是：第2到4列合并。

详细代码如下：

print(sheet1.merged_cells)
print(sheet1.cell_value(1,3))
print(sheet1.cell_value(4,3))
print(sheet1.cell_value(6,1))
运行结果如下：

640?wx_fmt=png

发现规律了没？是的，获取merge_cells返回的row和col低位的索引即可！ 于是可以这样批量获取：

详细代码如下：

merge = []
print(sheet1.merged_cells)
for (rlow,rhigh,clow,chigh) in sheet1.merged_cells:
    merge.append([rlow,clow])
for index in merge:
    print(sheet1.cell_value(index[0],index[1]))
运行结果跟上图一样，如下：

640?wx_fmt=png

Python读写Excel表格，就是这么简单粗暴又好用，如果觉得不错，对你工作中有帮助，动动手指分享给更多人哦。

声明：本文为作者投稿，版权归作者个人所有。

640?wx_fmt=gif640?wx_fmt=gif

'''