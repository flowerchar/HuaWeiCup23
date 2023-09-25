import pandas as pd

pd.set_option('display.max_columns',None)
df = pd.read_excel(r'./info/数据2.1 .xlsx') # , header=[0,1,2]
# df = pd.read_excel(r'./info/数据2.2 .xlsx')# , header=[0,1,2]

df.iloc[:, 26].fillna(df.iloc[:, 25], inplace=True)
df.iloc[:, 30].fillna(df.iloc[:, 29], inplace=True)
df.iloc[:, 34].fillna(df.iloc[:, 33], inplace=True)

# df.iloc[:, 27].fillna(df.iloc[:, 26], inplace=True)
# df.iloc[:, 31].fillna(df.iloc[:, 30], inplace=True)
# df.iloc[:, 35].fillna(df.iloc[:, 34], inplace=True)

df.to_excel('./info/2-1补充第二阶段复议分.xlsx',index=False)