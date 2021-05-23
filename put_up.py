import os
import pandas as pd


files_xls \
    = [


'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.01\\SubRNB_Nissan_New 2019.01.01-2019.01.28_upd_1.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.02\\SubRNB_Nissan_New 2019.01.02-2019.02.28_5day.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.03\\SubRNB_Nissan_New 2019.01.03-2019.03.31_5day.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.04\\SubRNB_Nissan_New 2019.01.04-2019.04.30_5day.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.05\\SubRNB_Nissan_New 2019.01.05-2019.05.31_5day.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.06\\SubRNB_Nissan_New 2019.01.06-2019.06.30_5day.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.07\\SubRNB_Nissan_New 2019.01.07-2019.07.31_5day.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.08\\SubRNB_Nissan_New 2019.01.08-2019.08.31_5day_Nissan.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Petrova\\2019\\Closing 2019.09\\SubRNB_Nissan_New 2019.01.09-2019.09.30 _5dayNissan.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Pricing_Retail\\Subsidies\\RNBank\\2019\\11\\SubRNB_Nissan_New 01.11.2019-30.11.2019-C_учетом_Датсуном.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\CFO\\Pricing_Retail\\Subsidies\\RNBank\\2019\\12\\12-2019\\SubRNB_Nissan_New 2019.01.12-2019.12.31 - 5 day _Datsun - без автомобиля сотрудника.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\01_2020\\Copy of SubRNB_Nissan_New - 01.01.2020-31.01.2020 - 5 day (002) - Version 2.0.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\02_2020\\SubRNB_Nissan_New 2020.01.02-2020.02 - day 5 - резерв - Version 3.0.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\03_2020\\03-2020\\SubRNB_Nissan_New 2020.01.03-2020.03.31- Day 5 - Version 2.0.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\04_2020\\SubRNB_Nissan_New 2020.01.04-2020.04.30 - Day 5.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\05_2020\\subrnb_nissan_day5_May2020_version1.0.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\06_2020\\nissan_subrnb_day5_june2020.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\07_2020\\nissan_subrnb_day5_july2020-Version1.0.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\08_2020\\Subrnb_Nissan_Aug_day5.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\09_2020\\Subrnb_September_Nissan_day5.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\10_2020\\Nissan_day5.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\11_2020\\Subrnb_Nissan_day5_2020-11.xlsx',
'I:\\0RU_RCI\\RCI_FIN\\subsidy\\bank_subs\\2020\\12_2020\\SUBRNB_Nissan_day5.xlsx'
    ]

df = pd.DataFrame()
print('ok')


for f in files_xls:
    data = pd.read_excel(f)
    df = df.append(data)

df_index = df.reset_index()

print(df_index)

df_index.to_excel('nissan_sub2019-2020.xlsx')


