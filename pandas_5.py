import pandas as pd
# 文本格式数据的读写
df = pd.read_csv('ex1.csv')
# print(df)
df = pd.read_table('ex1.csv',sep=',')
# print(df)
#自动分配列名
df = pd.read_csv('ex2.csv',header=None)
# print(df)
# 自己指定列名
names = ['a','b','c','d','message']
df = pd.read_csv('ex2.csv',names=names)
# print(df)
# 指定索引列
df = pd.read_csv('ex2.csv',names=names,
                 index_col='message')
# print(df)
# 多个列中形成一个分程索引
df = pd.read_csv('ex3.csv',
                 index_col=['key1','key2'])
# print(df)
# print(list(open('ex4.txt')))
# 使用空白或其他方式来分隔字段，可以使用正则表达式\s+
result = pd.read_table('ex4.txt',sep='\s+')
# print(result)
# 可以使用skiprows来过滤不需要的行
result = pd.read_csv('ex5.csv',skiprows=[0,2])
# print(result)
# 缺失值要么不显示，要么用一些标识值，默认情况，使用NA和NULL
result = pd.read_csv('ex6.csv')
# print(result)
# print(pd.isnull(result))
# 在字典中，每列可以指定不同的缺失值标识
sentinels = {'message':['foo','NA'],
             'something':['two']}
# print(pd.read_csv('ex6.csv',na_values=sentinels))
# 分块读入文本文件
# 为了分块读入文件，可以指定chunksize作为每一块的行数
dframe = pd.read_csv('ex7.csv',chunksize=50)
