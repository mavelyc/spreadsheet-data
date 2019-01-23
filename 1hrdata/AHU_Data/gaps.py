#python script used to fill iun the hourly gaps of the AHU data given
import xlsxwriter
import xlrd
import os

# file_name = raw_input("Name of file? ")
# newfile = raw_input("Name of new file? ")

# workbook = xlsxwriter.Workbook(newfile + ".xlsx")
# worksheet = workbook.add_worksheet()

# worksheet.write(0,0,"Date")
# worksheet.write(0,1,"Time")
# worksheet.write(0,2,"Value")

book = xlrd.open_workbook("NEW.xlsx")
sheet = book.sheet_by_index(0)

count = 1
val = sheet.cell(count,3).value
print val

# while (sheet.cell(count,1).value != ''):
#     print count
#     count+=1


# while(sheet.cell(i+1,1).value != ''):
#     #print sheet.cell(i+1,1).value
#     i+=1
#     # if(sheet.cell(i+1,1).value < sheet.cell(i,1).value):
#     #     if (sheet.cell(i+1,1).value != sheet.cell(i,1).value - 1):
#     #         while(sheet.cell(i+1,1).value != ''):
#     #             count+=1
#     #         print count

#     #else: #for next day
# print "hello"
    

# timeval = sheet.cell(1,2).value
# dateval = sheet.cell(1,3).value
# count = 1
# start = 1
# iterate = 1
# total=0
# while (iterate< data_points + 1):
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

        
# workbook.close()
#os.remove(file_name + ".xlsx")