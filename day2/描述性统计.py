import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# 读取Excel数据
df = pd.read_excel(r'./info/数据1.xlsx')  # 请将路径替换为您的Excel文件路径
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
# 描述性统计
print("描述性统计：")
print(df.describe())

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
