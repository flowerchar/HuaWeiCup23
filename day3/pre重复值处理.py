

import pandas as pd

# df = pd.read_excel(r'./info/数据2.1 .xlsx' )
df = pd.read_excel(r'./info/数据2.2 .xlsx' , header=[0,1,2])

duplicate_rows = df[df.duplicated()]
# 输出结果
if duplicate_rows.shape[0] == 0:
    print("表格中不存在重复的行。")
else:
    print("表格中存在重复的行。")