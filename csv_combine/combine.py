import pandas as pd
import glob

# #glob set up
# filetype = raw_input("Common name between all files you want to scan? ")
# #ending = raw_input("File type/endings? ")
# path = './' + filetype + '*.' + "xls"
# files = glob.glob(path)
 
allFiles = glob.glob("./*.csv")
#print(allFiles)


df_list = []
for f in allFiles:
    df = pd.read_csv(f)
    df.rename(columns={"Value (%)":f[2:-4],"Value (°C)":f[2:-4]}, inplace=True)
    df.drop_duplicates(subset="Time", keep="first",inplace=True)
    df.dropna(axis=0, how='any', thresh=None, subset=["Time"], inplace=True)
    df = df.reset_index()
    df.sort_values(by=['Time'])
    df = df.drop(columns=["index"])
    df_list.append(df)



final = pd.concat(df_list,sort=False,axis=1)
final.to_csv('final2.csv', index=False)
# writer = pd.ExcelWriter('final.xls')




# df0 = pd.read_csv('TL_DS570CTA01_H_EvacAmRT_H5_TL.csv')
# df1 = pd.read_csv('TL_DS570CTA01_T_Evac_T5_TL.csv')
# df = pd.concat([df0,df1],axis=1)

# df.to_csv('final.csv', index=False)