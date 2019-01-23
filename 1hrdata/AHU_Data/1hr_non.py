#non polling for multiple files
import xlrd
import xlsxwriter
import glob

#glob set up
filetype = raw_input("Common name between all files you want to scan? ")
ending = raw_input("File type/endings? ")
path = './' + filetype + '*.' + ending

files = glob.glob(path)

num_inputs = input("How many variables? ")

#intial write to new excel file
book = xlrd.open_workbook(files[0])
sheet = book.sheet_by_index(0)
first_file = sheet.cell(0,1).value

workbook = xlsxwriter.Workbook("TEMP.xlsx")
worksheet = workbook.add_worksheet()
worksheet.set_column(0,0,25)

for title in range(num_inputs):
    worksheet.write(0,title,'Var'+str(title+1))


cell_format = workbook.add_format()
cell_format.set_num_format('dd/mm/yyyy hh:mm')

k=1
for f in files:
    book = xlrd.open_workbook(f)
    sheet = book.sheet_by_index(0)
    j=0
    i=7
    while i<6007:
        if j == 0:
            worksheet.write(k,j,sheet.cell(i,j).value,cell_format)
        else:    
            val = sheet.cell(i,j).value
            worksheet.write(k,j,val)
        j+=1
        if j > num_inputs-1:
            j=0
            i+=1
            k+=1

for all in range(1,k):
    formula = '=HOUR(A' + str(all+1) + ')'
    formula2 = '=TEXT(A' + str(all+1) + ','+'"mm/dd/yy"'+')'
    worksheet.write(all,2,formula)
    worksheet.write(all,3,formula2)

    


workbook.close()