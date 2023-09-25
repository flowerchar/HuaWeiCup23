import pandas as pd


df = pd.read_excel('./info/2-2补充第二阶段复议分.xlsx')

# 计算第36列的数据
start_row = 2 # 开始行数
end_row = 9332  # 结束行数

# 遍历从第4行到第100行的每一行，计算第36列的值
for row in range(start_row, end_row-1 ):
    print([df.iloc[row, 8], df.iloc[row, 11], df.iloc[row, 14], df.iloc[row, 17], df.iloc[row, 20]])
    values_to_sum = [df.iloc[row, 8], df.iloc[row, 11], df.iloc[row, 14], df.iloc[row, 17], df.iloc[row, 20]]
    df.at[row, 36] = sum(values_to_sum)

df.to_excel('./info/2-2补充新的一列.xlsx', index=False)



# df = pd.read_excel('./info/2-1补充第二阶段复议分.xlsx')
#
# # 计算第36列的数据
# start_row = 2 # 开始行数
# end_row = 888  # 结束行数
#
# # 遍历从第4行到第100行的每一行，计算第36列的值
# for row in range(start_row, end_row-1 ):
#     print([df.iloc[row, 7], df.iloc[row, 10], df.iloc[row, 13], df.iloc[row, 16], df.iloc[row, 19]])
#     values_to_sum = [df.iloc[row, 7], df.iloc[row, 10], df.iloc[row, 13], df.iloc[row, 16], df.iloc[row, 19]]
#     df.at[row, 35] = sum(values_to_sum)
#
# df.to_excel('./info/2-1补充新的一列.xlsx', index=False)


