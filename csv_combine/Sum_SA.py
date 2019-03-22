import glob
import pandas as pd
from pandas import ExcelFile

flag = 0
list1 = []

for filename in glob.glob("C:/Users/mavelyc/Desktop/PRH_January_Data/*/*/*Data.xlsx"):
    print (filename)
    if (filename=="C:/Users/mavelyc/Desktop/PRH_January_Data\System05\D-06-70-CTA-08\Hourly_Data.xlsx"
        or filename=="C:/Users/mavelyc/Desktop/PRH_January_Data\System08\D-20N-70-CTA-02\Hourly_Data.xlsx"):continue
        #or filename=="C:/Users/mavelyc/Desktop/PRH_January_Data\System10\B1-06-70-CTA-04\Hourly_Data.xlsx"):continue
    if(flag==0):
        xl_workbook = pd.ExcelFile(filename)
        df = xl_workbook.parse("Sheet1")
        list1 = (df.iloc[:,5]+df.iloc[:,9]).tolist()
        flag=1
    else:
        xl_workbook = pd.ExcelFile(filename)
        df = xl_workbook.parse("Sheet1")
        newlist = (df.iloc[:,5]+df.iloc[:,9]).tolist()
        count=0
        for i in newlist:
            #print(i)
            tmp = list1[count]
            list1[count] = tmp+i
            count+=1
    print(list1)

# df2=pd.DataFrame({'Value': list1})
# wb = load_workbook('C:/Users/mavelyc/Desktop/PRH_January_Data/SUM_SA.xlsx')

# ws = wb['Sheet1']

# for index, row in df2.iterrows():
#     cell = 'C%d'  % (index + 2)
#     ws[cell] = row[0]

# wb.save('C:/Users/mavelyc/Desktop/PRH_January_Data/SUM_SA.xlsx.xlsx')

