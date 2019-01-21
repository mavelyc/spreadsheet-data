import xlsxwriter
import xlrd

workbook = xlsxwriter.Workbook('1hr_final_nonpoll.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0,"Date")
worksheet.write(0,1,"Time")
worksheet.write(0,2,"Value")

book = xlrd.open_workbook('1hr_tmp_nonpoll.xlsx')
sheet = book.sheet_by_index(0)

val = sheet.cell(1,2).value
count = 1
iterate = 1
total=0
while (iterate<6001):
    if (sheet.cell(iterate,2).value == val):
        tmp = sheet.cell(iterate,1).value
        tmp = tmp.encode('ascii')
        tmp = float(tmp)
        total += tmp
        iterate+=1
    else:
        worksheet.write(count,1,val)
        worksheet.write(count,0,sheet.cell(count,3).value)
        #print iterate,count
        final = total/(iterate-count)
        worksheet.write(count,2,final)
        count=iterate+1
        iterate=count
        val = sheet.cell(count,2).value

worksheet.write(count,1,val)
#print iterate,count
final = total/(iterate-count)
worksheet.write(count,2,final)

        
workbook.close()