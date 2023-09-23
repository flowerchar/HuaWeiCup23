import pandas as pd
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


print(max(score_list_1), min(score_list_1))
print(max(score_list_2), min(score_list_2))
print(max(score_list_3), min(score_list_3))
print(max(score_list_4), min(score_list_4))
print(max(score_list_5), min(score_list_5))

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