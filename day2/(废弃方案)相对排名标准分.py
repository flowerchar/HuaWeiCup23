import pandas as pd
import statistics
from copy import deepcopy
import json
import statistics
from collections import Counter
def find_percentile_reverse(arr, x):
    """
    计算数字 x 在降序列表 arr 中排在百分之一的位置。
    """
    count = 0  # 记录大于或等于 x 的元素个数
    total_elements = len(arr)

    for num in arr:
        if num >= x:
            count += 1
        else:
            break  # 由于列表是降序的，一旦遇到小于 x 的元素，可以停止计数

    percentile = (count / total_elements) * 100
    return percentile
def find_percentile(arr, x):
    """
    计算数字 x 在升序列表 arr 中排在百分之多少的位置。
    """
    count = 0  # 记录小于或等于 x 的元素个数
    total_elements = len(arr)

    for num in arr:
        if num <= x:
            count += 1
        else:
            break  # 由于列表是升序的，一旦遇到大于 x 的元素，可以停止计数

    percentile = (count / total_elements) * 100
    return percentile
#显示所有行
with open('data_raw.json', 'r') as json_file:
    data_dict = json.load(json_file)
with open('data_template.json', 'r') as json_file:
    data_template:dict = json.load(json_file)
pd.set_option('display.max_rows',None)
# TODO：修改路径
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

score_list_1 = []
score_list_2 = []
score_list_3 = []
score_list_4 = []
score_list_5 = []


for (index_1, row_1),(index_2, row_2),(index_3, row_3),(index_4, row_4),(index_5, row_5) in zip(special_1.iterrows(), special_2.iterrows(),special_3.iterrows(),special_4.iterrows(),special_5.iterrows()):
    for (column_1, value_1),(column_2, value_2),(column_3, value_3),(column_4, value_4),(column_5, value_5), in zip(row_1.items(), row_2.items(), row_3.items(), row_4.items(), row_5.items(), ):
        # print(index_1)
        current_expert_1 = value_1
        current_raw_1 = special_1_raw.iloc[index_1][0]
        data_list_1:list = data_dict.get(current_expert_1)
        data_list_1.sort(reverse=True)
        percentile_1 = find_percentile_reverse(data_list_1, current_raw_1)/100
        # print(percentile_1)



        current_expert_2 = value_2
        current_raw_2 = special_2_raw.iloc[index_2][0]
        data_list_2:list = data_dict.get(current_expert_2)
        data_list_2.sort(reverse=True)
        percentile_2 = find_percentile_reverse(data_list_2, current_raw_2)/100


        current_expert_3 = value_3
        current_raw_3 = special_3_raw.iloc[index_3][0]
        data_list_3:list = data_dict.get(current_expert_3)
        data_list_3.sort(reverse=True)
        percentile_3 = find_percentile_reverse(data_list_3, current_raw_3)/100

        current_expert_4 = value_4
        current_raw_4 = special_4_raw.iloc[index_4][0]
        data_list_4:list = data_dict.get(current_expert_4)
        data_list_4.sort(reverse=True)
        percentile_4 = find_percentile_reverse(data_list_4, current_raw_4)/100

        current_expert_5 = value_5
        current_raw_5 = special_5_raw.iloc[index_5][0]
        data_list_5:list = data_dict.get(current_expert_5)
        data_list_5.sort(reverse=True)
        percentile_5 = find_percentile_reverse(data_list_5, current_raw_5)/100

        s1 = (1 - percentile_1) * 100*(8/9)
        s2 = (1 - percentile_2) * 100*(8/9)
        s3 = (1 - percentile_3) * 100*(8/9)
        s4 = (1 - percentile_4) * 100*(8/9)
        s5 = (1 - percentile_5) * 100*(8/9)

        # x = (s1+s2+s3+s4+s5)*(8/9)
        score_list_1.append(s1)
        score_list_2.append(s2)
        score_list_3.append(s3)
        score_list_4.append(s4)
        score_list_5.append(s5)

        data_template.get(current_expert_1).append(s1)
        data_template.get(current_expert_2).append(s2)
        data_template.get(current_expert_3).append(s3)
        data_template.get(current_expert_4).append(s4)
        data_template.get(current_expert_5).append(s5)

# with open('data_std-经过方案二后的标准分.json', "w") as json_file:
#     json.dump(data_template, json_file)
# print(score_list_1)
# print(score_list_2)
# print(score_list_3)
# print(score_list_4)
# print(score_list_5)
# sum_index_list = []
abs_error = 0
# # # 计算总和并保存到列表中
# for i in range(len(score_list_1)):
#     total = score_list_1[i] + score_list_2[i] + score_list_3[i] + score_list_4[i] + score_list_5[i]  # 计算总和
#     index = i  # 当前元素的索引
#     sum_index_list.append((total, index, 0))  # 添加到列表中，第三项表示排序前的位置
#
# # 对列表按照第一项（总和）降序排序
# sorted_sum_index_list = sorted(sum_index_list, key=lambda x: x[0], reverse=True)
#
# # 更新排序后的位置信息（第三项）
# for i, item in enumerate(sorted_sum_index_list):
#     item_list = list(item)
#     item_list[2] = i
#     sorted_sum_index_list[i] = tuple(item_list)
#
# # 过滤出第二项小于28的元素并保存到 ultimate_result_list
# ultimate_result_list = [item for item in sorted_sum_index_list if item[1] < 28]
#
# # 打印排序前的前28个元素在排序后的位置
# print("排序前的前28个元素在排序后的位置：")
# for total, index, sorted_index in ultimate_result_list:
#     print(f"元素总和：{total}，排序前的索引：{index+1}，排序后的位置：{sorted_index+1}")
#     abs_error += abs(index - sorted_index)
# 创建一个空列表用于存储总和、索引和排序前的位置
# sum_index_list = []
#
# # 计算总和并保存到列表中
# for i in range(len(score_list_1)):
#     # 从每个列表中去除最大值和最小值（如果有多个最大值或最小值，则舍弃一个）
#     values_to_sum = [score_list_1[i], score_list_2[i], score_list_3[i], score_list_4[i], score_list_5[i]]
#     values_to_sum.remove(max(values_to_sum))
#     values_to_sum.remove(min(values_to_sum))
#
#     total = sum(values_to_sum)  # 计算总和
#     index = i  # 当前元素的索引
#     sum_index_list.append((total, index, 0))  # 添加到列表中，第三项表示排序前的位置
#
# # 对列表按照第一项（总和）降序排序
# sorted_sum_index_list = sorted(sum_index_list, key=lambda x: x[0], reverse=True)
#
# # 更新排序后的位置信息（第三项）
# for i, item in enumerate(sorted_sum_index_list):
#     item_list = list(item)
#     item_list[2] = i
#     sorted_sum_index_list[i] = tuple(item_list)
#
# # 过滤出第二项小于28的元素并保存到 ultimate_result_list
# ultimate_result_list = [item for item in sorted_sum_index_list if item[1] < 28]
#
# # 打印排序前的前28个元素在排序后的位置
# print("排序前的前28个元素在排序后的位置：")
# for total, index, sorted_index in ultimate_result_list:
#     print(f"元素总和：{total}，排序前的索引：{index+1}，排序后的位置：{sorted_index+1}")
#     abs_error += abs(index - sorted_index)
# 创建一个空列表用于存储总和、索引和排序前的位置
# sum_index_list = []
#
# # 计算总和并保存到列表中
# for i in range(len(score_list_1)):
#     values = [score_list_1[i], score_list_2[i], score_list_3[i], score_list_4[i], score_list_5[i]]  # 五个数值
#     median = statistics.median(values)  # 计算中位数
#     index = i  # 当前元素的索引
#     sum_index_list.append((median, index, 0))  # 添加到列表中，第三项表示排序前的位置
#
# # 对列表按照第一项（中位数）降序排序
# sorted_sum_index_list = sorted(sum_index_list, key=lambda x: x[0], reverse=True)
#
# # 更新排序后的位置信息（第三项）
# for i, item in enumerate(sorted_sum_index_list):
#     item_list = list(item)
#     item_list[2] = i
#     sorted_sum_index_list[i] = tuple(item_list)
#
# # 过滤出第二项小于28的元素并保存到 ultimate_result_list
# ultimate_result_list = [item for item in sorted_sum_index_list if item[1] < 28]
#
# # 打印排序前的前28个元素在排序后的位置
# print("排序前的前28个元素在排序后的位置：")
# for median, index, sorted_index in ultimate_result_list:
#     print(f"元素中位数：{median}，排序前的索引：{index+1}，排序后的位置：{sorted_index+1}")
#     abs_error += abs(index - sorted_index)
sum_index_list = []

# 计算总和并保存到列表中
for i in range(len(score_list_1)):
    values = [score_list_1[i], score_list_2[i], score_list_3[i], score_list_4[i], score_list_5[i]]  # 五个数值
    max_value = max(values)  # 最大值
    min_value = min(values)  # 最小值
    other_values = sum(values) - max_value - min_value  # 剩余三个值的和
    total = (max_value * 1/8) + (min_value * 1/8) + (other_values * 1/4)  # 计算总和
    index = i  # 当前元素的索引
    sum_index_list.append((total, index, 0))  # 添加到列表中，第三项表示排序前的位置

# 对列表按照第一项（总和）降序排序
sorted_sum_index_list = sorted(sum_index_list, key=lambda x: x[0], reverse=True)

# 更新排序后的位置信息（第三项）
for i, item in enumerate(sorted_sum_index_list):
    item_list = list(item)
    item_list[2] = i
    sorted_sum_index_list[i] = tuple(item_list)

# 过滤出第二项小于28的元素并保存到 ultimate_result_list
ultimate_result_list = [item for item in sorted_sum_index_list if item[1] < 28]

# 打印排序前的前28个元素在排序后的位置
print("排序前的前28个元素在排序后的位置：")
for total, index, sorted_index in ultimate_result_list:
    print(f"元素总和：{total}，排序前的索引：{index+1}，排序后的位置：{sorted_index+1}")
    abs_error += abs(index - sorted_index)
print(abs_error)
exit(0)
df.iloc[2:3+2015, 7] = score_list_1
df.iloc[2:3+2015, 10] = score_list_2
df.iloc[2:3+2015, 13] = score_list_3
df.iloc[2:3+2015, 16] = score_list_4
df.iloc[2:3+2015, 18] = score_list_5
df.to_excel('output相对.xlsx', index=False)

# print(max(score_list))
# print(min(score_list))
# print(sum(score_list)/len(score_list))
# print(len(score_list))
#
# count = Counter(score_list)
#
# # 找出众数
# most_common = count.most_common(1)
#
# # most_common返回一个列表，包含出现频率最高的元素及其频率
# if most_common:
#     mode, mode_count = most_common[0]
#     print(f'众数是 {mode}，出现次数为 {mode_count}')
# else:
#     print('列表为空，没有众数')
#
# print('中位数是',statistics.median(score_list))