import pandas as pd
import numpy as np

# 创建一个示例的 Series 和 DataFrame
s1 = pd.Series([0, 2, 1, 3])  # 假设 s1 的索引是 [0, 1, 2, 3]
data = np.random.randint(1, 10, size=(4, 5))  # 创建一个 4x5 的示例 DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

# 使用 Series 的索引选择 DataFrame 的第四列数据，并根据 Series 索引重新命名列
selected_data = df.iloc[:, 3].rename(s1)

print(df)
print('aaaa')
# 打印选择的数据
print(selected_data)
