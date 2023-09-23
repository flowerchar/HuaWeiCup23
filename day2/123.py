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

# 示例列表
Alist = [10, 20, 30, 40, 50, 60, 70, 80]

# 要查找的数字
x = 40

# 计算 x 在 Alist 中排在百分之多少的位置
result = find_percentile(Alist, x)/100

print(f"{x} 在列表中排在百分之{result:.2f}的位置")