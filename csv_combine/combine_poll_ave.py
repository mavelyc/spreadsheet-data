import pandas as pd

# #glob set up
# filetype = raw_input("Common name between all files you want to scan? ")
# #ending = raw_input("File type/endings? ")
# path = './' + filetype + '*.' + "xls"
# files = glob.glob(path)

filename = "final"
 
f = "./Book1.csv"

df = pd.read_csv(f)
df.rename(columns={"Value (%)":f[2:-4],"Value (°C)":f[2:-4]}, inplace=True)
#df.drop_duplicates(subset="Time", keep="first",inplace=True)
#df.dropna(axis=0, how='any', thresh=None, subset=["Time"], inplace=True)
df = df.reset_index()
df.sort_values(by=['Time'])
df = df.drop(columns=["index"])

df['Hour'] = pd.to_datetime(df['Time']).dt.hour
df["Ave_Time"] = ""
df["AVE "+f[2:-4]] = ""
hour_val = df['Hour'][0]
total = 0
count = 0
ave_tally = 0
date_index = 0
for index, row in df.iterrows():
    print (index)
    print (row[f[2:-4]])
    if (pd.isnull(row[f[2:-4]])): break
    if (row['Hour'] == hour_val):
        total += row[f[2:-4]]
        ave_tally+=1
    else:
        df.iloc[count, df.columns.get_loc('Ave_Time')] = df["Time"][date_index]
        ave = total/ave_tally
        df.iloc[count, df.columns.get_loc('AVE '+f[2:-4])] = ave
        hour_val = row['Hour']
        total=row[f[2:-4]]
        count += 1
        ave_tally =1
        date_index = index
    globindex = index
globindex+=1
df.iloc[count, df.columns.get_loc('Ave_Time')] = df["Time"][globindex-1]
ave = total/ave_tally
df.iloc[count, df.columns.get_loc('AVE '+f[2:-4])] = ave

df = df.drop(columns=["Time",f[2:-4],"Hour"])
df.to_csv(filename +".csv", index=False)
# writer = pd.ExcelWriter('final.xls')




# df0 = pd.read_csv('TL_DS570CTA01_H_EvacAmRT_H5_TL.csv')
# df1 = pd.read_csv('TL_DS570CTA01_T_Evac_T5_TL.csv')
# df = pd.concat([df0,df1],axis=1)

# df.to_csv('final.csv', index=False)