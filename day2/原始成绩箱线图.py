import matplotlib.pyplot as plt
import random
import json
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'
with open('data_raw.json', 'r') as json_file:
    data = json.load(json_file)
# 给定的字典，键是专家编号，值是评分列表

n = 10  # 这里可以根据需要设置抽样次数

# 存储所有抽样的数据
all_samples = []

# 存储专家编号的列表
expert_labels = []

# 随机抽样n次，将数据添加到all_samples列表中
for i in range(n):
    # 随机选择一个专家
    expert = random.choice(list(data.keys()))
    # 获取该专家的评分数据
    scores = data[expert]
    # 将数据添加到列表中
    all_samples.append(scores)
    # 将专家编号添加到专家编号的列表中
    expert_labels.append(expert)

# 创建箱线图
plt.figure()
plt.boxplot(all_samples)
plt.title(f'随机抽取{n}位评审专家的原始评分对比')
plt.xlabel('专家编码')
plt.ylabel('原始成绩')
plt.xticks(range(1, n+1), expert_labels)

# 显示箱线图
plt.show()