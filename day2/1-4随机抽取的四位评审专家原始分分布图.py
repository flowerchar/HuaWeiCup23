import matplotlib.pyplot as plt
import random
import json
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'

RAW_JSON = 'data_raw.json'
STD_JSON = 'data_std.json'
STD_JSON_1 = 'data_std-经过方案一后的标准分.json'
STD_JSON_2 = 'data_std-经过方案二后的标准分.json'

GREEN = '#7be196'
PINK = '#fa9c90'
BLUE = '#7c9dea'
ORANGE = '#f6af6b'

COLOR_MAP = {RAW_JSON:GREEN, STD_JSON:PINK, STD_JSON_1:BLUE, STD_JSON_2:ORANGE}

CURRENT_TYPE = RAW_JSON

with open(CURRENT_TYPE, 'r') as json_file:
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
# data = {'P90':[10,2,56,78,345,1]} # 这里data长度是97，而不是一个，我省去了
selected_experts = random.sample(data.items(), 4)

# 创建一个包含四个子图的图表
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('随机抽取的四位评审专家原始分分布图')
# x_values:int
# 绘制每个子图
for i, (expert, scores) in enumerate(selected_experts):
    row = i // 2
    col = i % 2
    x_values = range(len(scores))  # x轴的位置
    axs[row, col].bar(x_values, scores, alpha=0.6, color=COLOR_MAP[CURRENT_TYPE])
    # axs[row, col].hist(scores, bins=10, alpha=0.6)
    axs[row, col].set_title(expert)
    axs[row, col].set_xlabel('作品编号')
    axs[row, col].set_ylabel('原始分')

    # 设置x轴标签，每隔一定数量的数据点显示一个标签，并旋转标签
    label_step = max(1, len(x_values) // 10)  # 每隔10个数据点显示一个标签
    axs[row, col].set_xticks(x_values[::label_step])
    axs[row, col].set_xticklabels([f'{i + 1}' for i in x_values[::label_step]])
# # 设置x轴标签
# for ax in axs.flat:
#     ax.set_xticks(x_values)
#     ax.set_xticklabels([f'{i+1}' for i in range(len(scores))], rotation=45, ha='right')

# 调整子图之间的间距
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()