import xlrd
import xlwt

#intial write to new excel file


#read values
book = xlrd.open_workbook('Cx_Data SYS01 CTA Alim T4 H4 Sept1.xls')
sheet = book.sheet_by_index(0)
i = sheet.cell(7,1).value
#j = sheet.cell(1,1).value

print i