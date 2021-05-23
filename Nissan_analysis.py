import pandas as pd
import cx_Oracle as cx
import matplotlib.pyplot as plt

dsn = """(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)
(HOST=rnb-vmdwh-dbpr04.rci.renault.ru)(PORT=1521))
(ADDRESS=(PROTOCOL=TCP)(HOST=rnb-vmdwh-dbpr03.rci.renault.ru)(PORT=1521))
(LOAD_BALANCE= yes))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=DWHPR_DG)))
"""
connection = cx.connect("iz01340", "iz01340", dsn)

print('fine')
query = """
select app_number,
CREDIT_CONTRACT_NUM,
PRODUCT_NAME,
MODEL_CODE,
INTEREST_RATE,
EXPECTED_BANK_RATE,
CAR_PRICE,
LOAN_FOR_CAR_SUM,
TOTAL_FINANCE_AMOUNT,
credit_issue_date as credit_issue,
credit_closed_date as credit_close,
months_between(credit_closed_date,credit_issue_date) as fact_duration,

duration,

months_between(credit_closed_date,credit_issue_date)/duration AS fact_by_plan_duration,
total_finance_amount/car_price as loan_by_price,
Y_OF_FINANCING,
M_OF_FINANCING

from dwh.v_indicator_fpa
where brand='Nissan'
and NEW_USED='NEW'
and Y_OF_FINANCING in ('2019','2020')
           """

df_ind = pd.read_sql(query, con=connection)
print(1)

df_sub = pd.read_excel('Nissan_sub2019-2020.xlsx')

df_t = pd.merge(df_sub, df_ind, how='inner',
                left_on='app_number', right_on='APP_NUMBER')

print(df_t)

df_t.to_excel('Subs2019-2020.xlsx', sheet_name='vin_sub')

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



