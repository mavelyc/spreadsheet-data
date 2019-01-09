import xlrd
import xlsxwriter
import glob

#glob set up
path = './C*.xls'
files = glob.glob(path)

#intial write to new excel file
workbook = xlsxwriter.Workbook('final.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column(0,0,25)
worksheet.write(0,0,'Date')
worksheet.write(0,1,'Number')
worksheet.write(0,2,'Degrees')
worksheet.write(0,3,'Percent1')
worksheet.write(0,4,'Percent2')

cell_format = workbook.add_format()
cell_format.set_num_format('dd/mm/yyyy hh:mm')

#read values
k = 1
for f in files:
    book = xlrd.open_workbook(f)
    sheet = book.sheet_by_index(0)
    i = 7
    j = 0
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

workbook.close()