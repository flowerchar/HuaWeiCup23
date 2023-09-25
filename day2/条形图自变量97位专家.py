import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'
# 打开JSON文件
with open('data_raw.json', 'r') as file:
    # 加载JSON数据
    data = json.load(file)

experts = []
avg_score = []
for expert, scores in data.items():
    experts.append(expert)
    avg_score.append(sum(scores)/len(scores))

# 绘制条形图
# plt.xticks(range(len(experts)), experts, rotation=180)

plt.figure(figsize=(12, 6))  # 设置图形大小
plt.bar(experts, avg_score)  # 创建条形图
plt.xlabel('专家编码')  # x轴标签
plt.ylabel('原始成绩平均分')  # y轴标签
plt.title('专家原始成绩平均分条形图')  # 图表标题
# plt.xticks()
# 可选：如果你的专家编码很长，可以使用以下代码进行x轴标签的旋转，以避免重叠
plt.xticks(rotation=90)
plt.ylim(30, 100)
plt.show()  # 显示图表