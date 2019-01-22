#used to summarize data given at random times into hourly increment
import csv
import xlsxwriter
import xlrd

data_points = input("Number of data points? ") #you can change this value to a constant number of data points
fname = raw_input("Name of file? ") #you can change for a constant name of file

#intial write to new excel file
workbook = xlsxwriter.Workbook('1hr_tmp_nonpoll.xlsx')
worksheet = workbook.add_worksheet()

with open(fname) as csv_file:
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