import xlsxwriter
import xlrd
import os

data_points = input("Number of data points? ")
newfile = raw_input("Name of new file? ")

workbook = xlsxwriter.Workbook(newfile + ".xlsx")
worksheet = workbook.add_worksheet()

worksheet.write(0,0,"Date")
worksheet.write(0,1,"Time")
worksheet.write(0,2,"Value")

book = xlrd.open_workbook('1hr_tmp_nonpoll.xlsx')
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
os.remove("1hr_tmp_nonpoll.xlsx")