import json
import pandas as pd
# 指定JSON文件路径


# 打开JSON文件并加载数据到字典
with open('expert_average.json', 'r') as json_file:
    expert_average = json.load(json_file)
with open('expert_std_deviation.json', 'r') as json_file:
    expert_std_deviation = json.load(json_file)
with open('formatted_alpha_values.json', 'r') as json_file:
    formatted_alpha_values = json.load(json_file)
    formatted_alpha_values = json.loads(formatted_alpha_values)

# print(expert_average)
# print(expert_std_deviation)
# print(formatted_alpha_values)

#显示所有行
pd.set_option('display.max_rows',None)

df = pd.read_excel(r'./info/数据1.xlsx')
# special_n对应表格第一次评审成绩的专家几(一二三四五)的专家编号
special_1 = df.iloc[:, [5]][2:]
special_2 = df.iloc[:, [8]][2:]
special_3 = df.iloc[:, [11]][2:]
special_4 = df.iloc[:, [14]][2:]
special_5 = df.iloc[:, [17]][2:]

special_1_raw = df.iloc[:, [6]][:]
special_2_raw = df.iloc[:, [9]][:]
special_3_raw = df.iloc[:, [12]][:]
special_4_raw = df.iloc[:, [15]][:]
special_5_raw = df.iloc[:, [18]][:]

special_1_std = []
special_2_std = []
special_3_std = []
special_4_std = []
special_5_std = []

# print(special_1_raw.iloc[0][0])
# print(type(special_1_raw.iloc[0]))
for index, row in special_1.iterrows():
    for column, value in row.items():
        a = formatted_alpha_values.get(value)
        # a = 1
        b = expert_average.get(value)
        c = expert_std_deviation.get(value)
        ak = special_1_raw.iloc[index][0]
        x = a*(50 + 10*((ak-b)/c))
        special_1_std.append(x)

for index, row in special_2.iterrows():
    for column, value in row.items():
        a = formatted_alpha_values.get(value)
        # a = 1
        b = expert_average.get(value)
        c = expert_std_deviation.get(value)
        ak = special_2_raw.iloc[index][0]
        x = a*(50 + 10*((ak-b)/c))
        special_2_std.append(x)

for index, row in special_3.iterrows():
    for column, value in row.items():
        a = formatted_alpha_values.get(value)
        # a = 1
        b = expert_average.get(value)
        c = expert_std_deviation.get(value)
        ak = special_3_raw.iloc[index][0]
        x = a*(50 + 10*((ak-b)/c))
        special_3_std.append(x)

for index, row in special_4.iterrows():
    for column, value in row.items():
        a = formatted_alpha_values.get(value)
        # a = 1
        b = expert_average.get(value)
        c = expert_std_deviation.get(value)
        ak = special_4_raw.iloc[index][0]
        x = a*(50 + 10*((ak-b)/c))
        special_4_std.append(x)

for index, row in special_5.iterrows():
    for column, value in row.items():
        a = formatted_alpha_values.get(value)
        # a = 1
        b = expert_average.get(value)
        c = expert_std_deviation.get(value)
        ak = special_5_raw.iloc[index][0]
        x = a*(50 + 10*((ak-b)/c))
        special_5_std.append(x)

# print(len(special_1_std))
# print(df.shape[0])

# # 确保插入的数据长度与行数匹配  以下代码貌似没用@@@
# if len(special_1_std) <= (df.shape[0] - 3):  # 减去前三行的行数
#     start_row = 3  # 从第四行开始插入数据
#     end_row = start_row + len(special_1_std)  # 结束插入的行数
#
#     # 将新数据插入到第八列，从第四行到第2018行
#     df.iloc[start_row:end_row, 7] = special_1_std  # 7表示第八列，索引从0开始
#
#     # 将修改后的DataFrame保存为新的Excel文件
#     df.to_excel('output.xlsx', index=False)
#
#     print("数据已保存到 output.xlsx")
# else:
#     print("插入的数据长度大于可用的行数") @@@

df.iloc[2:3+2015, 7] = special_1_std
df.iloc[2:3+2015, 10] = special_2_std
df.iloc[2:3+2015, 13] = special_3_std
df.iloc[2:3+2015, 16] = special_4_std
df.iloc[2:3+2015, 18] = special_5_std
df.to_excel(r'./info/经过方案一更新标准差后的数据1.xlsx', index=False)

print(special_1_std)
print(special_2_std)
print(special_3_std)
print(special_4_std)
print(special_5_std)
