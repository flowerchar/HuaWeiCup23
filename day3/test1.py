import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import json
# 指定JSON文件路径
rcParams['font.family'] = 'SimHei'
#显示所有行
pd.set_option('display.max_rows',None)
# TODO：修改路径
df = pd.read_excel(r'./info/2-2补充第二阶段复议分.xlsx', header=[0,1,2])
# special_n对应表格第一次评审成绩的专家几(一二三四五)的专家编号
special_1 = df.iloc[:, [8]]
special_2 = df.iloc[:, [11]]
special_3 = df.iloc[:, [14]]
special_4 = df.iloc[:, [17]]
special_5 = df.iloc[:, [20]]


special_1_std = []
special_2_std = []
special_3_std = []
special_4_std = []
special_5_std = []

# print(special_1_raw.iloc[0][0])
# print(type(special_1_raw.iloc[0]))
for index, row in special_1.iterrows():
    for column, value in row.items():
        special_1_std.append(value)

for index, row in special_2.iterrows():
    for column, value in row.items():
        special_2_std.append(value)
for index, row in special_3.iterrows():
    for column, value in row.items():
        special_3_std.append(value)
for index, row in special_4.iterrows():
    for column, value in row.items():
        special_4_std.append(value)
for index, row in special_5.iterrows():
    for column, value in row.items():
        special_5_std.append(value)

sum_std_list = []
for a, b, c, d, e in zip(special_1_std, special_2_std, special_3_std, special_4_std, special_5_std):
    sum_std_list.append(sum([a,b,c,d,e]))
# print(sum_std_list)


sub_list = list(df.iloc[:, [23]].values)

one_dim_list = list(np.array(sub_list).flatten())
# print(one_dim_list)
# print(sum_std_list)
combined_list = [(a, b) for a, b in zip(sum_std_list, one_dim_list)]
# print(combined_list)
# sum_std_list.sort()
sorted_combined_list = sorted(combined_list, key=lambda x: x[0])
# print(len(sorted_combined_list))

selected_list = sorted_combined_list[:9320]

# 计算每个块的大小
chunk_size = len(selected_list) // 20

# 使用列表推导式将列表分成 20 个块（最后一块可能不满）
chunks = [selected_list[i:i + chunk_size] for i in range(0, len(selected_list), chunk_size)]
print(sorted_combined_list)
json_string = json.dumps(sorted_combined_list)
with open('my_list.json', 'w') as file:
    file.write(json_string)
exit(0)
y_values = [item[1] for item in sorted_combined_list]  # 因变量：从每个小元组中提取第二项数值
x_values = list(range(1, len(sorted_combined_list) + 1))  # 自变量：从1到9329的递增数列

# 创建散点图
plt.scatter(x_values, y_values, marker='o',s=1, color='b', label='散点图')

# 添加标题和标签
plt.title('散点图示例')
plt.xlabel('名次')
plt.ylabel('极差均值')

# 添加图例
plt.legend()

# 显示散点图
plt.show()