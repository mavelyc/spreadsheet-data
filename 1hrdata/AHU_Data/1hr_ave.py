#used to summarize data given at random times into hourly increment
import csv
import xlsxwriter
import xlrd
import os

data_points = input("Number of data points? ") #you can change this value to a constant number of data points
fname = raw_input("Name of file? ") #you can change for a constant name of file

#intial write to new excel file
workbook = xlsxwriter.Workbook('TEMP.xlsx')
worksheet = workbook.add_worksheet()

with open(fname + ".csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for time,value in csv_reader:
        if line==0:
            worksheet.write(line,0,"Time")
            worksheet.write(line,1,"Value")
        else:
            worksheet.write(line,0,time)
            worksheet.write(line,1,value)
        line+=1

for i in range(1,data_points + 1):
    formula = '=HOUR(A' + str(i+1) + ')'
    formula2 = '=TEXT(A' + str(i+1) + ','+'"mm/dd/yy"'+')'
    worksheet.write(i,2,formula)
    worksheet.write(i,3,formula2)

workbook.close()

print "--------------------------------------------------------------------------"
print "SAVE TEMP.XLSX FILE BEFORE CONTINUING!!"
print "--------------------------------------------------------------------------"

newfile = raw_input("Name of new file? ")

workbook = xlsxwriter.Workbook(newfile + ".xlsx")
worksheet = workbook.add_worksheet()

worksheet.write(0,0,"Date")
worksheet.write(0,1,"Time")
worksheet.write(0,2,"Value")

book = xlrd.open_workbook('TEMP.xlsx')
sheet = book.sheet_by_index(0)

timeval = sheet.cell(1,2).value
dateval = sheet.cell(1,3).value
count = 1
start = 1
iterate = 1
total=0
while (iterate< data_points + 1):
    if (sheet.cell(iterate,2).value == timeval and sheet.cell(iterate,3).value == dateval):
        tmp = sheet.cell(iterate,1).value
        tmp = tmp.encode('ascii')
        tmp = float(tmp)
        total += tmp
        iterate+=1
    else:
        worksheet.write(count,1,timeval)
        worksheet.write(count,0,sheet.cell(start,3).value)
        #print iterate,count
        final = total/(iterate-start)
        #print final
        worksheet.write(count,2,final)
        start=iterate
        count+=1
        timeval = sheet.cell(start,2).value
        dateval = sheet.cell(start,3).value
        total=0

worksheet.write(count,1,timeval)
worksheet.write(count,0,sheet.cell(start,3).value)
final = total/(iterate-start)
worksheet.write(count,2,final)

        
workbook.close()
os.remove("TEMP.xlsx")