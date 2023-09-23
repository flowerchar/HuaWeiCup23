import matplotlib.pyplot as plt
import json
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'
with open('data_raw.json', 'r') as json_file:
    data = json.load(json_file)
# 假设数据存放在名为data的字典中，其中键是专家编码，值是成绩列表

# 计算每位专家的平均原始成绩
average_scores = {expert: sum(scores) / len(scores) for expert, scores in data.items()}

# 提取专家编码和对应的平均原始成绩
experts = list(average_scores.keys())
average_values = list(average_scores.values())

# 创建折线图
plt.figure(figsize=(12, 6))
plt.plot(experts, average_values, marker='o', linestyle='-')
plt.title('专家平均原始成绩折线图')
plt.xlabel('专家编码')
plt.ylabel('平均原始成绩')
plt.xticks(rotation=90)  # 使x轴标签更清晰可读
plt.tight_layout()
plt.show()





