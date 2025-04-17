import pandas as pd
import sys

# 将数据写入文本格式
data = pd.read_csv('ex6.csv')
print(data)
# 使用to_csv方法将数据导出为逗号分隔符的文件
# data.to_csv('out_0.csv')
# 写入到控制台，na_rep属性设置缺失值，sep属性是分隔符
data.to_csv(sys.stdout, na_rep='NULL', sep='|',
            index=False, columns=['a', 'b', 'c'])
