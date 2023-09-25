import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'
df = pd.read_excel('./info/2-2补充第二阶段复议分.xlsx', header=[0,1,2])
subset_df = df.iloc[:1500]
data = subset_df.iloc[:, 4]
# 使用 Seaborn 绘制密度图
sns.kdeplot(data, shade=True)

# 添加标题和标签
plt.title("Kernel Density Plot")
plt.xlabel("Values")
plt.ylabel("Density")

# 显示密度图
plt.show()