import matplotlib.pyplot as plt
import random
import json
from matplotlib import rcParams

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

rcParams['font.family'] = 'SimHei'
# with open('data_raw.json', 'r') as json_file:
# with open('data_std.json', 'r') as json_file:
# with open('data_std-经过方案一后的标准分.json', 'r') as json_file:
with open(CURRENT_TYPE, 'r') as json_file:
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
# plt.figure()
plt.boxplot(all_samples ,boxprops={'color': COLOR_MAP[CURRENT_TYPE]})
# plt.title(f'随机抽取{n}位评审专家的原始评分对比')
# plt.xlabel('专家编码')
# plt.ylabel('原始成绩')
# plt.title(f'随机抽取{n}位评审专家的标准分评分对比')
# plt.xlabel('专家编码')
# plt.ylabel('标准分成绩')
# plt.title(f'方案一-随机抽取{n}位评审专家的标准分评分对比')
# plt.xlabel('专家编码')
# plt.ylabel('方案一标准分成绩')
plt.title(f'方案二-随机抽取{n}位评审专家的标准分评分对比')
plt.xlabel('专家编码')
plt.ylabel('方案二标准分成绩')
plt.xticks(range(1, n+1), expert_labels)

# 显示箱线图
plt.savefig(r'../pictures/方案二-随机抽取10位评审专家的标准分评分对比.png')
plt.show()
