import matplotlib.pyplot as plt
import random
import json
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'
with open('data_raw.json', 'r') as json_file:
    data = json.load(json_file)

# # 随机选择四个键值对
# selected_experts = random.sample(data.items(), 4)
#
# # 创建一个包含四个子图的图表
# fig, axs = plt.subplots(2, 2, figsize=(12, 8))
# fig.suptitle('随机抽取的四位评审专家原始分分布图')
#
# # 绘制每个子图
# for i, (expert, scores) in enumerate(selected_experts):
#     row = i // 2
#     col = i % 2
#     x = list(range(1, len(scores) + 1))
#     y = scores
#     axs[row, col].scatter(x, y)
#     axs[row, col].set_title(expert)
#     axs[row, col].set_xlabel('原始分顺序')
#     axs[row, col].set_ylabel('原始分')
#
# # 调整子图之间的间距
# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()

# 随机选择四个键值对
selected_experts = random.sample(data.items(), 4)

# 创建一个包含四个子图的图表
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('随机抽取的四位评审专家原始分分布直方图')

# 绘制每个子图
for i, (expert, scores) in enumerate(selected_experts):
    row = i // 2
    col = i % 2
    axs[row, col].hist(scores, bins=10, alpha=0.6)
    axs[row, col].set_title(expert)
    axs[row, col].set_xlabel('原始分')
    axs[row, col].set_ylabel('频次')

# 调整子图之间的间距
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()