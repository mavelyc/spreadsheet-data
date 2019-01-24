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
    # formula5 = '=HOUR('+ newdate + str(top+1) + ')'
    # formula6 = '=TEXT('+ newdate + str(top+1) + ','+'"mm/dd/yy"'+')'
    # formula7 = '=' + newletter_hour + str(top+1) + '&' + newletter_date + str(top+1)
    worksheet.write(top,num_inputs,formula)
    worksheet.write(top,num_inputs+1,formula2)
    worksheet.write(top,num_inputs+2,formula3)
    # worksheet.write(top,num_inputs+5,formula5)
    # worksheet.write(top,num_inputs+6,formula6)
    # worksheet.write(top,num_inputs+7,formula7)

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

workbook.close()





print "--------------------------------------------------------------------------"
print "SAVE TEMP.XLSX FILE BEFORE CONTINUING!!"
print "--------------------------------------------------------------------------"


wait = input("????")


#intial write to new excel file
# book = xlrd.open_workbook(files[0])
# sheet = book.sheet_by_index(0)
# first_file = sheet.cell(0,1).value

workbook = xlsxwriter.Workbook("final.xlsx")
worksheet = workbook.add_worksheet()
# worksheet.set_column(0,0,25)

for title in range(num_inputs):
    worksheet.write(0,title,'Var'+str(title+1))



workbook.close()

#Below calculates and writes the average
# column = 1
# while (column < num_inputs):
#     if (sheet.cell(iterate,2).value == timeval and sheet.cell(iterate,3).value == dateval):
#         tmp = sheet.cell(iterate,1).value
#         tmp = tmp.encode('ascii')
#         tmp = float(tmp)
#         total += tmp
#         iterate+=1
#     else:
#         worksheet.write(count,1,timeval)
#         worksheet.write(count,0,sheet.cell(start,3).value)
#         #print iterate,count
#         final = total/(iterate-start)
#         #print final
#         worksheet.write(count,2,final)
#         start=iterate
#         count+=1
#         timeval = sheet.cell(start,2).value
#         dateval = sheet.cell(start,3).value
#         total=0

# worksheet.write(count,1,timeval)
# worksheet.write(count,0,sheet.cell(start,3).value)
# final = total/(iterate-start)
# worksheet.write(count,2,final)

# startdate = raw_input("What is the start date in mm/dd/yyyy? ")
# worksheet.write(1,5,startdate,cell_format)
# cell_format1 = workbook.add_format()
# cell_format1.set_num_format("mm/dd/yyyy hh:mm")
# for date in range(2,num_dates*24+1):
#     formula4 = '=$F'+str(date)+'+TIME(1,0,0)'
#     worksheet.write(date,5,formula4,cell_format1)

#workbook.close()

# wait = raw_input ("Continue? ")

# tempbook = xlrd.open_workbook("TEMP.xlsx")
# tempsheet = tempbook.sheet_by_index(0)

# print tempsheet.cell(1,2).value