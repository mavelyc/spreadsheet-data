#non polling for multiple files
import xlrd
import xlsxwriter
import glob
import os

#glob set up
filetype = raw_input("Common name between all files you want to scan? ")
ending = raw_input("File type/endings? ")
startdate = raw_input("What is the start date in mm/dd/yyyy? ")
path = './' + filetype + '*.' + ending

files = glob.glob(path)

num_inputs = input("How many variables? ")
num_dates = input("How many different dates? ")

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
cell_format.set_num_format('mm/dd/yyyy hh:mm')

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

letter_hour = chr(ord('A')+num_inputs)
letter_date = chr(ord('A')+num_inputs+1)
newdate = chr(ord('A')+num_inputs+4)
newletter_hour = chr(ord('A')+num_inputs+5)
newletter_date = chr(ord('A')+num_inputs+6)
for top in range(1,k):
    formula = '=HOUR(A' + str(top+1) + ')'
    formula2 = '=TEXT(A' + str(top+1) + ','+'"mm/dd/yy"'+')'
    formula3 = '=' + letter_hour + str(top+1) + '&' + letter_date + str(top+1)
    worksheet.write(top,num_inputs,formula)
    worksheet.write(top,num_inputs+1,formula2)
    worksheet.write(top,num_inputs+2,formula3)

for rows in range(1,num_dates*24+1):
    formula5 = '=HOUR('+ newdate + str(rows+1) + ')'
    formula6 = '=TEXT('+ newdate + str(rows+1) + ','+'"mm/dd/yy"'+')'
    formula7 = '=' + newletter_hour + str(rows+1) + '&' + newletter_date + str(rows+1)
    worksheet.write(rows,num_inputs+5,formula5)
    worksheet.write(rows,num_inputs+6,formula6)
    worksheet.write(rows,num_inputs+7,formula7)

worksheet.write(1,num_inputs+4,startdate,cell_format)
initial_date_column = chr(ord('A')+num_inputs+4)
for date in range(2,num_dates*24+1):
    formula4 = '=$'+ initial_date_column +str(date)+'+TIME(1,0,0)'
    worksheet.write(date,num_inputs+4,formula4,cell_format)

    worksheet.write(top,num_inputs+5,formula5)
    worksheet.write(top,num_inputs+6,formula6)
    worksheet.write(top,num_inputs+7,formula7)

serial_letter1 = chr(ord('A')+num_inputs+2)
serial_letter2 = chr(ord('A')+num_inputs+7)
curr_col = chr(ord('A')+num_inputs+8)
for var in range(1,num_inputs):
    var_letter = chr(ord('A')+var)
    for aveif in range(1,num_dates*24+1):
        formula8 = '=IFERROR(AVERAGEIF($'+serial_letter1 + '$2:$' + serial_letter1 + '$' + str(k) + ',' + serial_letter2 + str(aveif+1) + ',$' + var_letter + '$2:$' + var_letter + '$' + str(k) +'),' + curr_col + str(aveif) + ')'  
        worksheet.write(aveif,num_inputs+8,formula8)

workbook.close()



print "--------------------------------------------------------------------------"
print "SAVE TEMP.XLSX FILE BEFORE CONTINUING!!"
print "--------------------------------------------------------------------------"


# wait = input("????")

# book = xlrd.open_workbook("TEMP.xlsx")
# sheet = book.sheet_by_index(0)

# workbook = xlsxwriter.Workbook(first_file + ".xlsx")
# worksheet = workbook.add_worksheet()
# # worksheet.set_column(0,0,25)

# cell_format = workbook.add_format()
# cell_format.set_num_format('mm/dd/yyyy hh:mm')

# for title in range(num_inputs):
#     worksheet.write(0,title,'Var'+str(title+1))

# for rows in range(1,num_dates*24+1):
#     val = sheet.cell(rows,num_inputs+4).value
#     worksheet.write(rows,0,val,cell_format)



# workbook.close()