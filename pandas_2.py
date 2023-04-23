import pandas as pd

# DataFrame表示的是矩阵的数据表，它包含已排序的列的集合，每个列可以是不同的值类型。
# DataFrame既有行索引也有列索引
# 它可以被视为一个共享相同索引的Series字典
# DataFrame的构建最常用的方式是利用包含等长度列表或Numpy数组的字典来形成
data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002,2003],
    'pop':[1.5,1.7,3.6,2.4,2.9,3.2]
}
frame = pd.DataFrame(data)
print(frame)
# head方法将会只选头部的五行
print(frame.head())
# 如果传入的列不包含在字典中，将会在结果中出现缺失值
frame1 = pd.DataFrame(data,columns=['year','state','pop','debt'])
print(frame1)
print(frame1['year'])
# 只有在列名是有效的Python变量名时有效
print(frame1.year)
print(frame1)
print(frame1.T)


