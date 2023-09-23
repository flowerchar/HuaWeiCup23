import matplotlib.pyplot as plt
import random
import json
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'
with open('data_raw.json', 'r') as json_file:
    data = json.load(json_file)
# 从数据中随机选择四位评委的数据
selected_experts = random.sample(list(data.keys()), 4)

# 创建密度图
plt.figure(figsize=(10, 6))

# 绘制不同评委的密度曲线
for expert in selected_experts:
    scores = data[expert]
    plt.hist(scores, bins=20, density=True, alpha=0.6, label=expert)

plt.title('不同评委的原始成绩密度图')
plt.xlabel('分数')
plt.ylabel('频次')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()