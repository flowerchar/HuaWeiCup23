import pandas as pd

# 读取原始Excel文件
original_excel_file = './info/数据1.xlsx'
df = pd.read_excel(original_excel_file)

# 复制数据到新的Excel文件
new_excel_file = './info/模板.xlsx'
df.to_excel(new_excel_file, index=False)

print(f'Excel文件已成功复制为 {new_excel_file}')