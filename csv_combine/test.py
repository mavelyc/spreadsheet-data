#testing before implementation into combine.py

import pandas as pd

df=pd.read_csv("TL_DS570CTA01_H_EvacAmRT_H5_TL.csv")
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
#df.to_csv("help.csv")
# print(df['Hour'][5999])
# if (pd.isna(df['Hour'][6000])): print ("True")
# else: print ("False")
# #print (df)

for index, row in df.iterrows():
    print(index['Hour'],row['Hour'])