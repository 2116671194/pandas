import pandas as pd
import sys
import numpy as np
# 将数据写入文本格式
data = pd.read_csv('ex6.csv')
print(data)
# 使用to_csv方法将数据导出为逗号分隔符的文件
# data.to_csv('out_0.csv')
# 写入到控制台，na_rep属性设置缺失值，sep属性是分隔符
data.to_csv(sys.stdout,na_rep='NULL',sep='|',
            index=False,columns=['a','b','c'])
# Series也有to_csv方法
datas = pd.date_range('1/1/2022',periods=7)
ts = pd.Series(np.arange(7),index=datas)
# ts.to_csv('out_2.csv')
# 对于任何带有单字符分隔符的文件，可以使用python的内建csv模块

