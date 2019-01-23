import xlrd
import xlsxwriter
import glob

#glob set up
path = './C*.xls'
files = glob.glob(path)

num_inputs = input("How many variables? ")

#intial write to new excel file
book = xlrd.open_workbook(files[0])
sheet = book.sheet_by_index(0)
first_file = sheet.cell(0,1).value

workbook = xlsxwriter.Workbook(first_file + ".xlsx")
worksheet = workbook.add_worksheet()
worksheet.set_column(0,0,25)

for title in range(num_inputs):
    worksheet.write(0,title,'Var'+str(title+1))


# worksheet.write(0,0,'Date')
# worksheet.write(0,1,'Var1')
# worksheet.write(0,2,'Var2')
# worksheet.write(0,3,'Percent1')
# worksheet.write(0,4,'Percent2')

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
            total = 0
            count = i
            for num in range(12):
                tmp = sheet.cell(count,j).value
                tmp = tmp.encode('ascii')
                if tmp == '': tmp = 0
                else: tmp = float(tmp)
                total= total + tmp
                count+=1
            ave = total/12.0
            worksheet.write(k,j,ave)
        j+=1
        if j > num_inputs-1:
            j=0
            i+=12
            k+=1

workbook.close()