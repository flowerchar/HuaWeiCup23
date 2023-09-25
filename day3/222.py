# # 示例数据（根据你的需求替换 A）
# A = [i for i in range(74)]
#
# # 生成字符串列表
# string_list = [f'前{13+value}%-{13+value + 0.5}%' for value in A]
#
# # 打印生成的字符串列表
# print(string_list)

import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5]
string_list = ['前13%-13.5%', '前18%-18.5%', '前23%-23.5%', '前28%-28.5%', '前33%-33.5%']

# 绘制折线图
plt.plot(range(len(data)), data, marker='o', linestyle='-', color='b', label='折线图')

# 设置横坐标的标签
plt.xticks(range(len(string_list)), string_list, rotation=90)

# 添加标题和标签
plt.title('Line Chart Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# 显示图例
plt.legend()

# 显示折线图
plt.show()