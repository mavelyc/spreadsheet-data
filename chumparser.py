import xlrd
import xlsxwriter

#intial write to new excel file
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0,'Hello')

workbook.close()


#set row for headers
""" row = sheet.row(0)
row.write(0,'Date')
row.write(1,'Numbers')
row.write(2, 'degrees')
row.write(3,'percent1')
row.write(4,'percent2') """


#read values
""" book = xlrd.open_workbook('Cx_Data SYS01 CTA Alim T4 H4 Sept1.xls')
sheet = book.sheet_by_index(0)
i = sheet.cell(7,1).value """
#j = sheet.cell(1,1).value

#print i