import pandas as pd
import glob

# #glob set up
# filetype = raw_input("Common name between all files you want to scan? ")
# #ending = raw_input("File type/endings? ")
# path = './' + filetype + '*.' + "xls"
# files = glob.glob(path)
 
# allFiles = glob.glob("./*.csv")

# list_ = []

# for file_ in allFiles:
#     df = pd.read_csv(file_,index_col=None, header=0)
#     list_.append(df)
# print (list_)

df0 = pd.read_csv('TL_DS570CTA01_H_EvacAmRT_H5_TL.csv')
df1 = pd.read_csv('TL_DS570CTA01_T_Evac_T5_TL.csv')
df = pd.concat([df0,df1],axis=1)

df.to_csv('final.csv', index=False)