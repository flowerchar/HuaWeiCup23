# 假设有五个没有规律的示例列表 A、B、C、D、E（长度相同）
A = [6, 18, 3, 12, 9, 27, 15, 21, 24, 30]
B = [7, 22, 11, 5, 25, 14, 10, 28, 16, 4]
C = [20, 29, 8, 19, 1, 13, 26, 23, 2, 17]
D = [36, 33, 37, 38, 34, 31, 32, 35, 39, 40]
E = [47, 44, 41, 45, 43, 46, 42, 48, 49, 50]

# 创建一个空列表用于存储总和、索引和排序前的位置
sum_index_list = []

# 计算总和并保存到列表中
for i in range(len(A)):
    total = A[i] + B[i] + C[i] + D[i] + E[i]  # 计算总和
    index = i  # 当前元素的索引
    sum_index_list.append((total, index, 0))  # 添加到列表中，第三项表示排序前的位置

# 对列表按照第二项（索引）降序排序
sorted_sum_index_list = sorted(sum_index_list, key=lambda x: x[1], reverse=True)

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
    print(f"元素总和：{total}，排序前的索引：{index}，排序后的位置：{sorted_index}")
