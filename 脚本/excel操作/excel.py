import xlrd
import xlwt

def read_excel():
    wordbook_excel = xlrd.open_workbook("test.xlsx")
    result_excel = xlwt.Workbook(encoding="ascii")
    wsheet = result_excel.add_sheet("sheet name")
    sheet_num = wordbook_excel.nsheets
    y = 0
    for m in range(0, sheet_num):
        sheet = wordbook_excel.sheet_by_index(m)  # 读取源excel文件第m个sheet的内容
        nrowsnum = sheet.nrows  # 获取该sheet的行数
        for i in range(0, nrowsnum):
            date = sheet.row(i)  # 获取该sheet第i行的内容
            for n in range(0, len(date)):
                aaa = str(date[n])  # 把该行第n个单元格转化为字符串，目的是下一步的关键字比对
                if aaa.find('关键字') > 0:  # 进行关键字比对，包含关键字返回1，否则返回0
                    y = y + 1
                    for j in range(len(date)):
                        wsheet.write(y, j, sheet.cell_value(i, j))  # 该行包含关键字，则把它所有单元格依次写入入新生成的excel的第y行
                else:
                    wsheet.write(y, i, sheet.cell_value(i, i))
    result_excel.save('jieguo.xlsx')  # 保存新生成的Excel


if __name__ == '__main__':
    read_excel()