#testing before implementation into combine.py

import pandas as pd

df=pd.read_csv("Input.csv")
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
df[""] = ""
df["Ave_Time"] = ""
df["Val"] = ""
# print(df['Hour'][5999])
# if (pd.isna(df['Hour'][6000])): print ("True")
# else: print ("False")
# #print (df)

hour_val = df['Hour'][0]
total = 0
count = 0
ave_tally = 0
globindex=0
for index, row in df.iterrows():
    if (row['Hour'] == hour_val):
        total += row['Value (%)']
        ave_tally+=1
    else:
        df.iloc[count, df.columns.get_loc('Ave_Time')] = df["Time"][index-1]
        ave = total/ave_tally
        df.iloc[count, df.columns.get_loc('Val')] = ave
        hour_val = row['Hour']
        total=row['Value (%)']
        count += 1
        ave_tally =1
    globindex = index
globindex+=1
df.iloc[count, df.columns.get_loc('Ave_Time')] = df["Time"][globindex-1]
ave = total/ave_tally
df.iloc[count, df.columns.get_loc('Val')] = ave
df.to_csv("Output.csv")