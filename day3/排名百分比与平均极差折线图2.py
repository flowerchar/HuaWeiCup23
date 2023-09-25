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

selected_list = sorted_combined_list[:9200]

# 计算每个块的大小
chunk_size = 46

# 使用列表推导式将列表分成 20 个块（最后一块可能不满）
chunks = [selected_list[i:i + chunk_size] for i in range(0, len(selected_list), chunk_size)]
# print(sorted_combined_list)
# 打印分成的块数和每个块的长度
print(f"分成了 {len(chunks)} 个块")
# for i, chunk in enumerate(chunks):
#     print(f"块 {i + 1} 长度: {len(chunk)}")

# 指定块的大小
chunk_size = 46

# 计算均值的函数
def calculate_q3(chunk):
    # 提取块中的第二项（数值）
    values = [item[1] for item in chunk]

    # 使用 numpy 计算上四分位数（Q3）
    q3 = np.percentile(values, 75)

    return q3

# 使用列表推导式计算每个块的均值
means = [calculate_q3(sorted_combined_list[i:i+chunk_size]) for i in range(0, len(selected_list), chunk_size)]
print(len(means))
new_list = means[26:-100]
# # 打印均值列表
# print(len(means))
# exit(0)
# [f'前{13+value}%-{13+value + 0.5}%' for value in [i for i in range(len(new_list))]]
string_list = [f'前{13+value}%-{13+value + 0.5}%' for value in [i for i in range(len(new_list))]]
plt.plot(string_list, new_list, marker='o', linestyle='-', color='b', label='折线图')
plt.xticks(range(len(string_list)), string_list, rotation=90)
# plt.hist(new_list, bins= 74,edgecolor='black', alpha=0.7)
# plt.bar(range(len(new_list)), new_list, color='b', label='条形图')
# 添加标题和标签
plt.title('折线图')
plt.xlabel('区间')
plt.ylabel('上四分位数')

# 添加图例
plt.legend()

# 显示折线图
plt.show()

# TODO 切成两百分，丢掉前26份和后一百份