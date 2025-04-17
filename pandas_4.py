# 函数应用和映射
import pandas as pd
import numpy as np

# NumPy的通用函数(逐元素数组方法)对pandas对象也有效
frame = pd.DataFrame(np.random.randn(4,3), columns=list('bdc'),index=['Utah','Ohio','Texas','Oregon'])
print(frame)
# 计算绝对值
print(np.abs(frame))
# 另一个常用的操作是将函数应用到一行或一列的一维数组上，
# DataFrame的apply方法可以实现这个功能
f = lambda x : x.max() - x.min()
print(frame.apply(f,axis=0))
print(frame.apply(f,axis=1))
# 传递给apply的函数并不一定要返回一个标量值，
# 也可以返回带有多个值的Series
def f(x):
    return pd.Series([x.min(),x.max(),x.sum()], index=['min','max','sum'])
print(frame.apply(f,axis=0))
print(frame.apply(f,axis=1))
# 排序和排名
# 如果需要按行或列索引进行字典型排序，
# 需使用sort_index方法
obj = pd.Series(range(4), index=['d','a','b','c'])
print(obj)
# 按索引排序
print(obj.sort_index())
# 按值排序
print(obj.sort_values())
# 在DataFrame上你可以在各轴上按照索引排序
frame = pd.DataFrame(np.arange(8).reshape((2,4)), index=['three','one'], columns=['d','a','b','c'])
print(frame.sort_index(axis=1,ascending=False))

frame = pd.DataFrame({'b':[4,7,-3,2], 'a':[0,1,0,1]})
print(frame)
print(frame.sort_values(by='b'))
print(frame.sort_values(by=['a','b']))
# Series和DataFrame的rank方法是实现排名的方法
# 默认情况下,rank通过将平均排名分配到每个组来打破平级关系
obj = pd.Series([7,-5,7,4,2,0,4])
print(obj)
# method='first':谁先出现谁的排名靠前
print(obj.rank(method='first'))
# method的='min':取在顺序排名中最小的那个排名作为该值的排名
# 会出现名次跳空
print(obj.rank(method='min'))
# method = 'max':取在顺序排名中最大的那个排名作为
# 该值的排名,会出现名次跳空
print(obj.rank(method='max'))
# method='dense':相同成绩的同学排名相同,其他依次加1,
# 不会出现名次跳空的情况
print(obj.rank(method='dense'))
# method='average':成绩相同时,取顺序排名中
# 所有名次之和除以该成绩的个数,即为该成绩的名次
print(obj.rank(method='average'))
# 含有重复标签的轴索引
obj = pd.Series(range(5),index=['a','a','b','b','c'])
print(obj)
# 该属性判断索引是否唯一
print(obj.index.is_unique)
print(obj['a'])
df = pd.DataFrame(np.random.randn(4,3), index=['a','a','b','b'])
print(df)
print(df.loc['b'])
# 描述性统计的概述与计算
df = pd.DataFrame([[1.4,np.nan],
                   [7.1,-4.5],
                   [np.nan,np.nan],
                   [0.75,-1.3]], index=['a','b','c','d'], columns=['one','two'])
print(df)
print(df.sum())
# 通过禁用skipna属性来实现不排除Nan值
print(df.mean(axis=1,skipna=False))
# 唯一值、计数和成员属性
obj = pd.Series(['c','a','d','a','a','b','b','c','c'])
# 获取Series中的唯一值
print(obj.unique())
# 获取Series中值的个数
print(obj.value_counts())
# isin执行向量化的成员属性检查
mask = obj.isin(['b','c'])
print(mask)
print(obj[mask])
# 与isin相关的Index.get_indexer方法，
# 可以提供一个索引数组，
# 这个索引数组可以将可能非唯一值数组转换为另一个唯一值数组：
to_match = pd.Series(['c','a','b','b','c','a'])
unique_vals = pd.Series(['c','b','a'])
print(pd.Index(unique_vals).get_indexer(to_match))
