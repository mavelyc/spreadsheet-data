#used to summarize data given at random times into hourly increment
import csv
import xlsxwriter

#intial write to new excel file
workbook = xlsxwriter.Workbook('1hr_final_nonpoll.xlsx')
worksheet = workbook.add_worksheet()

with open('TL_B10670CTA02_T_Alim_T4_TL.csv') as csv_file:
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

for i in range(1,6001):
    formula = '=HOUR(A' + str(i+1) + ')'
    worksheet.write(i,2,formula)

count = 1
while(count<6002):
    
        


# worksheet.set_column(0,0,25)
# worksheet.write(0,0,'Time')
# worksheet.write(0,1,'Data')

# cell_format = workbook.add_format()
# cell_format.set_num_format('dd/mm/yyyy hh:mm')

# #read values
# k = 1
# for f in files:
#     book = xlrd.open_workbook(f)
#     sheet = book.sheet_by_index(0)
#     i = 7
#     j = 0
#     while (i<295):
#         if j==0:
#             worksheet.write(k,j,sheet.cell(i,j).value, cell_format)
#         else: 
#             total = 0
#             count = i
#             for num in range(12):
#                 tmp = sheet.cell(count,j).value
#                 tmp = tmp.encode('ascii')
#                 tmp = float(tmp)
#                 total= total + tmp
#                 count+=1
#             ave = total/12.0
#             worksheet.write(k,j,ave)
#         j+=1
#         if j > 4:
#             j=j%5
#             i+=12
#             k+=1

workbook.close()