import xlrd
import xlsxwriter

#intial write to new excel file
workbook = xlsxwriter.Workbook('final.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0,'Date')
worksheet.write(0,1,'Number')
worksheet.write(0,2,'Degrees')
worksheet.write(0,3,'Percent1')
worksheet.write(0,4,'Percent2')


#read values
book = xlrd.open_workbook('Cx_Data SYS01 CTA Alim T4 H4 Sept1.xls')
sheet = book.sheet_by_index(0)
i = sheet.cell(7,1).value
j = sheet.cell(1,1).value
print i
worksheet.write(1,0,str(i))

workbook.close()