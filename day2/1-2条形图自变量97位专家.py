import json
import matplotlib.pyplot as plt
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

CURRENT_TYPE = STD_JSON
# 打开JSON文件
# with open('data_raw.json', 'r') as file:
with open(CURRENT_TYPE, 'r') as file:
    # 加载JSON数据
    data = json.load(file)
print(data)
# exit(0)
experts = []
avg_score = []
for expert, scores in data.items():
    experts.append(expert)
    avg_score.append(sum(scores)/len(scores))

# 绘制条形图
# plt.xticks(range(len(experts)), experts, rotation=180)

plt.figure(figsize=(12, 6))  # 设置图形大小
plt.bar(experts, avg_score, color=COLOR_MAP[CURRENT_TYPE])  # 创建条形图
plt.xlabel('专家编码')  # x轴标签
plt.ylabel('标准分成绩平均分')  # y轴标签
plt.title('专家标准分成绩平均分条形图')  # 图表标题

# plt.ylabel('标准分成绩平均分')  # y轴标签
# plt.title('专家标准分平均分条形图')  # 图表标题
# plt.xticks()
# 可选：如果你的专家编码很长，可以使用以下代码进行x轴标签的旋转，以避免重叠
plt.xticks(rotation=90)
plt.ylim(30, 100)
plt.savefig(r'../pictures/专家标准分成绩平均分条形图.png')
plt.show()  # 显示图表