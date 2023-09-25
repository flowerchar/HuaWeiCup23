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

CURRENT_TYPE = STD_JSON_2
with open(CURRENT_TYPE, 'r') as json_file:
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