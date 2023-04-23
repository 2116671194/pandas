# pandas是用来处理表格型或异质型数据的
import pandas as pd

#Series:是一种一维的数组型对象，它包含了一个值序列，并包含数据标签(索引),最简单的序列可由一个数组形成
obj = pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
print(obj.index)
# 通常需要创建一个索引序列，用于标识每个数据点
obj2 = pd.Series([2,-4,6,-8],index=['a','b','c','d'])
print(obj2)
print(obj2.index)
# 根据索引获取值
print(obj2['a'])
# 索引列表传入获取值
print(obj2[['b','c','d']])
# 利用布尔值对数组进行过滤
print(obj2[obj2 > 0])
print(obj2 * 2)
# 可以认为Series是一个长度固定且有序的字典
print('b' in obj2)
print('e' in obj2)
# 用字典生成Series
s = {'one':1, 'two':2, 'three':3, 'four':4}
obj3 = pd.Series(s)
print(obj3)
index = ['zero','one','three','five']
obj4 = pd.Series(s,index=index)
print(obj4)
#pandas中缺失值用Nan代替，可以使用isnull和notnull函数检查缺失数据
print(pd.isnull(obj4))
print(pd.notnull(obj4))
# Series对象自身和其索引都有name属性、这个特性与pandas其他重要功能集成在一起
obj4.name = 'number'
obj4.index.name = 'state'
print(obj4)
# Series的索引可以通过按位置赋值的方式进行改变
obj = pd.Series([4,7,-5,3])
obj.index = ['a','b','c','d']
print(obj)