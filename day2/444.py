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

# print(len([88, 85, 80, 78, 76, 74, 74, 74, 74, 72, 72, 72, 70, 70, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 66, 66, 66, 65, 65, 65, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 62, 62, 62, 62, 61, 60, 60, 60, 60, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 57, 55, 55, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 48, 48, 45, 45, 45, 45, 45, 40, 40, 40, 40, 40, 40, 40, 35, 35, 35, 35, 30, 30,30,30,30,30]))
print(find_percentile([88, 85, 80, 78, 76, 74, 74, 74, 74, 72, 72, 72, 70, 70, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 66, 66, 66, 65, 65, 65, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 62, 62, 62, 62, 61, 60, 60, 60, 60, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 57, 55, 55, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 48, 48, 45, 45, 45, 45, 45, 40, 40, 40, 40, 40, 40, 40, 35, 35, 35, 35, 30, 30,30,30,30,30],74))