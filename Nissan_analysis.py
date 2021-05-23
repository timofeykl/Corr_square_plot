import pandas as pd
import cx_Oracle as cx
import matplotlib.pyplot as plt

dsn = """!!!
"""
connection = cx.connect("!!!", dsn)

# print('fine')
# query = """
# !!!

# duration,

# months_between(!!!)/!!! AS fact_by_plan_duration,
# total_finance_amount/car_price as loan_by_price,
# Y
# M

#            """

df_ind = pd.read_sql(query, con=connection)
print(1)

df_sub = pd.read_excel('!!!.xlsx')

df_t = pd.merge(df_sub, df_ind, how='inner',
                left_on='app_number', right_on='APP_NUMBER')

print(df_t)

df_t.to_excel('!!!', sheet_name='vin_sub')

df_corr = df_t.corr()

#print(df_corr)

sqr = plt.figure(figsize=(20,20))
plt.matshow(df_t.corr(), fignum = sqr.number)
plt.xticks(range(df_t.select_dtypes(['number']).shape[1]), df_t.select_dtypes(['number']).columns, fontsize=15, rotation=45)
plt.yticks(range(df_t.select_dtypes(['number']).shape[1]), df_t.select_dtypes(['number']).columns, fontsize=15)

hb = plt.colorbar()
hb.ax.tick_params(labelsize=20)
plt.title('Mat_cor', fontsize=15)

plt.show()


#df_corr.to_excel('SUBS2019-2020_CORR.xlsx', sheet_name='corr')



