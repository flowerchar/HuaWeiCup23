import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import json
rcParams['font.family'] = 'SimHei'
df = pd.read_excel('./info/2-2补充第二阶段复议分.xlsx', header=[0,1,2])
subset_df = df.iloc[:1500]

# 假设你有一个名为 df 的 DataFrame

# 计算第27列减去第26列的绝对值，保存到变量 A
A = (subset_df.iloc[:, 27] - subset_df.iloc[:, 26]).abs()

# 计算第31列减去第30列的绝对值，保存到变量 B
B = (subset_df.iloc[:, 31] - subset_df.iloc[:, 30]).abs()

# 计算第35列减去第34列的绝对值，保存到变量 C
C = (subset_df.iloc[:, 35] - subset_df.iloc[:, 34]).abs()

# 计算 (A + B + C) / 3，保存到变量 D
D = (A + B + C) # / 3

# 计算 D 除以第4列的数据
xxx = subset_df.iloc[:, 4]
result = D / subset_df.iloc[:, 4]

filtered_series = result[result!=0]
second_std_score = subset_df.iloc[:,4]
data = {
    'X':list(second_std_score[filtered_series.index].values),
    'Y':list(filtered_series.values)
}
print(data)
with open('./info/data2-1.json', "w") as json_file:
    json.dump(data, json_file)
# print(second_std_score[filtered_series.index].values)
# exit(0)
# 打印结果
# print(filtered_series)
# ssss = second_std_score[filtered_series.index].values
# aaaaa = filtered_series.values
plt.scatter(second_std_score[filtered_series.index].values, filtered_series.values)

# 添加标题和坐标轴标签
plt.title('2-2Scatter Plot')
plt.xlabel('第二次评审标准分极差')
plt.ylabel('偏移量')

# 显示散点图
plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import rcParams
# rcParams['font.family'] = 'SimHei'
# df = pd.read_excel('./info/2-1补充第二阶段复议分.xlsx', header=[0,1,2])
# subset_df = df.iloc[:240]
#
# # 假设你有一个名为 df 的 DataFrame
#
# # 计算第27列减去第26列的绝对值，保存到变量 A
# A = (subset_df.iloc[:, 26] - subset_df.iloc[:, 25]).abs()
#
# # 计算第31列减去第30列的绝对值，保存到变量 B
# B = (subset_df.iloc[:, 30] - subset_df.iloc[:, 29]).abs()
#
# # 计算第35列减去第34列的绝对值，保存到变量 C
# C = (subset_df.iloc[:, 34] - subset_df.iloc[:, 33]).abs()
#
# # 计算 (A + B + C) / 3，保存到变量 D
# D = (A + B + C) #/ 3
#
# # 计算 D 除以第4列的数据
# result = D / subset_df.iloc[:, 3]
#
# filtered_series = result[result!=0]
# second_std_score = subset_df.iloc[:, 3]
# print(second_std_score[filtered_series.index].values)
# # 打印结果
# # print(filtered_series.index)
# # X = subset_df[]
# plt.scatter(second_std_score[filtered_series.index].values, filtered_series.values)
#
# # 添加标题和坐标轴标签
# plt.title('2-1.Scatter Plot')
# plt.xlabel('第二次评审标准分极差')
# plt.ylabel('偏移量')
#
# # 显示散点图
# plt.show()