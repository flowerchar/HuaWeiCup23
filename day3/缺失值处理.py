
import pandas as pd
# 显示所有列
pd.set_option('display.max_columns',None)
# df = pd.read_excel(r'./info/数据2.1 .xlsx', header=[0,1,2])
df = pd.read_excel(r'./info/数据2.2 .xlsx', header=[0,1,2])
# df = pd.read_excel(r'./info/数据2.2 .xlsx' )
column_indices_to_exclude_1 = [3, 4, 23,24,25,26,27,28,29, 30,31,32,33 ,34]  # 替换为你要排除的列的序号 数据2.1排除的
column_indices_to_exclude_2  = [4,5,24,25,26,27,28,29,30,31,32,33,34,35]
# 使用iloc来删除列，同时指定axis=1表示删除列，这里通过更改 column_indices_to_exclude_改变
df_filtered = df.drop(df.columns[column_indices_to_exclude_2], axis=1)
# print(df_filtered)

# 检查df_filtered中是否存在缺失值
if df_filtered.isnull().any().any():
    result = "有缺失值"
else:
    result = "数据完整"

# 输出结果
print(result)
# 这段代码首先使用 .isnull().any().any() 来检查DataFrame中是否存在任何缺失值。如果存在任何一个缺失值，就会返回"有缺失值"，否则返回"数据完整"。最后，将结果打印出来。





