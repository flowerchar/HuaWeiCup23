import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import json
# 读取Excel数据
pd.set_option('display.max_rows',None)
df = pd.read_excel(r'./info/数据1.xlsx', header=[0,1,2])  # 请将路径替换为您的Excel文件路径
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
with open('data_raw.json', 'r') as json_file:
    data = json.load(json_file)
# 获取最短列的长度
min_length = min(len(value) for value in data.values())
# 创建一个字典，将每列的数据截断到最短列的长度
data_truncated = {key: value[:min_length] for key, value in data.items()}
# 将字典转换为 DataFrame
df = pd.DataFrame(data_truncated)
print(df.describe())

df.describe().to_excel('原始成绩描述性统计.xlsx', index=True)
exit(0)
# 绘制直方图
df.plot(kind='hist', bins=10, alpha=0.5, legend=True)
plt.xlabel('原始成绩')
plt.ylabel('频数')
plt.title('原始成绩分布直方图')
plt.show()

# 绘制箱线图
df.plot(kind='box', vert=False)
plt.xlabel('原始成绩')
plt.title('原始成绩箱线图')
plt.show()
