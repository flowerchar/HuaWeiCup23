import pandas as pd
# 显示所有列
pd.set_option('display.max_columns',None)
# df = pd.read_excel(r'./info/数据2.1 .xlsx', header=[0,1,2])
df = pd.read_excel(r'./info/数据2.2 .xlsx', header=[0,1,2])
column_indices_to_exclude_1 = [3, 4, 23,24,25,26,27,28,29, 30,31,32,33 ,34]  # 替换为你要排除的列的序号 数据2.1排除的
column_indices_to_exclude_2  = [4,5,24,25,26,27,28,29,30,31,32,33,34,35]
# 使用iloc来删除列，同时指定axis=1表示删除列，这里通过更改 column_indices_to_exclude_改变
df_filtered = df.drop(df.columns[column_indices_to_exclude_2], axis=1)
print(df_filtered)
# print(df_filtered)
# 使用applymap方法将每列中的元素类型转换为字符串并去重

# 初始化变量来存储不一致的列和位置
inconsistent_columns = []
first_inconsistent_index = None

# 遍历每一列
for column in df_filtered.columns:
    # 获取当前列的第一个元素类型
    first_element_type = type(df_filtered[column].iloc[0])

    # 获取当前列的值（去除列索引名）
    column_values = df_filtered[column].values

    # 检查当前列的每个元素是否与第一个元素类型一致
    if not all(isinstance(value, first_element_type) for value in column_values):
        inconsistent_columns.append(column)
        first_inconsistent_index = next(
            i for i, value in enumerate(column_values) if not isinstance(value, first_element_type))
        break

# 输出结果
if not inconsistent_columns:
    print("每列元素类型一致")
else:
    print(f"以下列的元素类型不一致：{inconsistent_columns}")
    print(f"第一个不一致元素的位置是：{first_inconsistent_index}")