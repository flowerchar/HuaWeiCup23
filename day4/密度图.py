import pandas as pd

pd.set_option('display.max_columns',None)
df = pd.read_excel(r'./info/数据1.xlsx', header=[0,1,2]) # , header=[0,1,2]
special_1 = df.iloc[:28, [0, 1]]
# special_2 = df.iloc[:, [8]]
# special_3 = df.iloc[:, [11]]
# special_4 = df.iloc[:, [14]]
# special_5 = df.iloc[:, [17]]
print(special_1)