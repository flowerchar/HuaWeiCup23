# -*- coding: utf-8 -*-
# 开发者：顾昕健
# 开发时间：2023/9/24 17:00
import os
# import PySide2
import pandas as pd
import matplotlib.pyplot as plt


# dirname = os.path.dirname(PySide2.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

# 读取Excel文件，并指定要读取的工作表名称
df = pd.read_excel(r'D:\PycharmProjects\git\问题2\newdata2.1.xlsx')
# 获取第四行到第243行的数据范围，第一次评审范围，并选择第极差列,第四列
data = df.iloc[2:242, [7, 10, 13, 16, 19]]
# 获取对应的名次范围
data2 = df.iloc[2:242,1]
# 获取第一列最终成绩
data3 = df.iloc[2:242,0]

# 计算各列的均值
mean_values = data.mean(axis=1)
mean=mean_values.tolist()

# 名次部分转换为列表
mc = data2.tolist()
mc_int = [int(x) for x in mc]

# 最终成绩转换为列表
zz = data3.tolist()


# 绘制折线图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为系统自带的黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
plt.plot(mc_int, mean)
plt.xlabel('名次')
plt.ylabel('标准分均值')
plt.title('第一次评审标准分均值成绩图')
plt.grid(True)
plt.savefig('第一次评审标准分均值成绩图.png')
plt.show()

# 绘制折线图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为系统自带的黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
plt.plot(mc_int, zz)
plt.xlabel('名次')
plt.ylabel('最终成绩图')
plt.title('第二次评审最终成绩图')
plt.grid(True)
plt.savefig('第二次评审最终成绩图.png')
plt.show()