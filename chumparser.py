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

cell_format = workbook.add_format()
cell_format.set_num_format('dd/mm/yyyy hh:mm AM/PM')

#read values
book = xlrd.open_workbook('Cx_Data SYS01 CTA Alim T4 H4 Sept1.xls')
sheet = book.sheet_by_index(0)
i = 7
j = 0
k = 1
while (i<295):
    if j==0:
        worksheet.write(k,j,sheet.cell(i,j).value, cell_format)
    else: 
        worksheet.write(k,j,sheet.cell(i,j).value)
    j+=1
    if j > 4:
        j=j%5
        i+=1
        k+=1


""" 

i = sheet.cell(7,0).value
j = sheet.cell(8,0).value
worksheet.write(1,0,i, cell_format)
worksheet.write(2,0,j,cell_format) """

workbook.close()