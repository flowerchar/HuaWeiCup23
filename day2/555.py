import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'
# # 示例数据
# categories = ['A', 'B', 'C', 'D']
# values = [15, 24, 30, 18]
#
# # 绘制垂直柱状图
# plt.bar(categories, values, color='green')  # 设置柱状图颜色为绿色
# plt.title('柱状图示例')
# plt.xlabel('类别')
# plt.ylabel('值')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# 生成一些示例数据
data = np.random.randn(1000)  # 随机生成1000个数据点

# 绘制直方图
plt.hist(data, bins=30, density=True, color='blue')  # 设置直方图颜色为蓝色
plt.title('直方图示例')
plt.xlabel('值')
plt.ylabel('密度')
plt.show()
