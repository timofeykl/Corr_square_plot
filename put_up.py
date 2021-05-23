import os
import pandas as pd


files_xls \
    = [

#list of excel files here
    ]

df = pd.DataFrame()
print('ok')


for f in files_xls:
    data = pd.read_excel(f)
    df = df.append(data)

df_index = df.reset_index()

print(df_index)

df_index.to_excel('
                  #to certain excel file                  
                  ')


