import pandas as pd
from copy import deepcopy
import json
#显示所有行
pd.set_option('display.max_rows',None)
df = pd.read_excel(r'./info/经过方案一更新标准差后的数据1.xlsx')
# special_n对应表格第一次评审成绩的专家几(一二三四五)的专家编号
special_1 = df.iloc[:, [5]][2:]
special_2 = df.iloc[:, [8]][2:]
special_3 = df.iloc[:, [11]][2:]
special_4 = df.iloc[:, [14]][2:]
special_5 = df.iloc[:, [17]][2:]
# 初始化一个空字典用于存放合并结果
merged_dict = {}
# 遍历每个字典并合并值
for d in [special_1.value_counts(), special_2.value_counts(), special_3.value_counts(), special_4.value_counts(), special_5.value_counts()]:
    for key, value in d.items():
        # 使用 .get() 方法获取键对应的值，如果键不存在则默认为0
        merged_dict[key] = merged_dict.get(key, 0) + value
new_merged_dict = {str(key[0]): value for key, value in merged_dict.items()}
# print(new_merged_dict)
# print("合并后的字典:", merged_dict)
# print(sum(list(merged_dict.values())))
# print(len(merged_dict))

# merged_dict_list是一个字典，键是专家编号，值是空列表   一定要用深度拷贝deepcopy
# merged_dict_list_raw是一个字典，键是专家编号，值是该专家对应的每次打出的原始成绩
# merged_dict_list_avg是一个字典，键是专家编号，值是该专家对应的每次打出的标准差成绩
merged_dict_list = {key: [] for key in new_merged_dict.keys()}
# print(merged_dict_list)
print(type(merged_dict_list))
with open('data_template.json', "w") as json_file:
    json.dump(merged_dict_list, json_file)
exit(0)
merged_dict_list_raw = deepcopy(merged_dict_list)
merged_dict_list_avg = deepcopy(merged_dict_list)

# 遍历所有专家编号，如果这一次编号出现在special_n中，那么把此次的原始成绩跟标准差成绩加入到对应列表，因此有五个循环
for k, v in merged_dict_list.items():
    for s1k, s1v in special_1.iterrows():
        if k == s1v[0]:
            merged_dict_list_raw[k].append(df.iloc[s1k, 6])
            merged_dict_list_avg[k].append(df.iloc[s1k, 7])
    for s2k, s2v in special_2.iterrows():
        if k == s2v[0]:
            merged_dict_list_raw[k].append(df.iloc[s2k, 9])
            merged_dict_list_avg[k].append(df.iloc[s2k, 10])
    for s3k, s3v in special_3.iterrows():
        if k == s3v[0]:
            merged_dict_list_raw[k].append(df.iloc[s3k, 12])
            merged_dict_list_avg[k].append(df.iloc[s3k, 13])
    for s4k, s4v in special_4.iterrows():
        if k == s4v[0]:
            merged_dict_list_raw[k].append(df.iloc[s4k, 15])
            merged_dict_list_avg[k].append(df.iloc[s4k, 16])
    for s5k, s5v in special_5.iterrows():
        if k == s5v[0]:
            merged_dict_list_raw[k].append(df.iloc[s5k, 18])
            merged_dict_list_avg[k].append(df.iloc[s5k, 19])

print(merged_dict_list_raw)
print(merged_dict_list_avg)

# 放开注释将字典序列化成json持久保存
# json_string_raw = json.dumps(merged_dict_list_raw)
json_string_avg = json.dumps(merged_dict_list_avg)
# with open('data_raw.json', 'w') as json_file:
#     json_file.write(json_string_raw)
with open('data_std-经过方案一后的标准分.json', 'w') as json_file:
    json_file.write(json_string_avg)