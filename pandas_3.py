# 基本功能
import numpy as np
import pandas as pd
# 重建索引
obj = pd.Series([4.5, 7.2, -5.3, 3.6],
                index=['d', 'b', 'c', 'a'])
print(obj)
obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)
obj3 = pd.Series(['blue','purple','yellow'],
                 index=[0,2,4])
print(obj3)
# method可选参数允许我们使用诸如ffill等方法在重建索引时插值，
# ffill方法会将值前向填充
obj4 = obj3.reindex(range(6),method='ffill')
print(obj4)
# 在DataFrame中reindex可以改变行索引、列索引、也可以同时改变两者
frame = pd.DataFrame(data=np.arange(9).reshape((3,3)),
                     index=['a','c','d'],
                     columns=['Ohio','Texas','California'])
print(frame)
frame2 = frame.reindex(['a','b','c','d'])
print(frame2)
state = ['Texas','Utah','California']
print(frame.reindex(columns=state))
# 轴向上删除条目
obj = pd.Series(data = np.arange(5),
                index = ['a','b','c','d','e'])
print(obj)
print(obj.drop(['c','d']))
data = pd.DataFrame(data=np.arange(16).reshape((4,4)),
                    index=['Ohio','Colorado','Utah','New York'],
                    columns=['one','two','three','four'])
print(data)
print(data.drop(['Colorado','Utah'],axis=0))
print(data.drop(['two'],axis=1))
print(data.drop(['two'],axis='columns'))
# 索引、选择与过滤
# Series的索引与NumPy数组索引的功能类似，
# 但Series的索引值可以不仅仅是整数
obj = pd.Series(np.arange(4.),index=['a','b','c','d'])
print(obj)
print(obj[1])
print(obj['b'])
print(obj[[1,3]])
print(obj[['b','c']])
print(obj[2:4])
print(obj['a':'c'])
print(obj[obj < 2])
# 可以使用以上方法修改Series相应的部分
obj['b':'c'] = 5
print(obj)
data = pd.DataFrame(data=np.arange(16).reshape((4,4)),
                    index=['Ohio','Colorado','Utah','New York'],
                    columns=['one','two','three','four'])
print(data)
# 使用单个值或序列，可以从DataFrame中索引出一个或多个列
print(data['two'])
print(data[['three','one']])
# 行索引
print(data[:2])
print(data[2:])
# 可以根据一个布尔值数组切片或选择数据
print(data[data['three'] > 5])
print(data < 5)
data[data < 5] = 0
print(data)
# 使用loc和iloc选择数据
# 他们允许你使用轴标签（ loc）或整数标签（ iloc）以NumPy风格的语法
# 从 DataFrame 中选出数组的行和列的子集
# 通过标签选出单行多列的数据
print(data)
print(data.loc['Colorado',['two','three']])
# 使用整数标签iloc进行类似的数据选择
print(data.iloc[1,[1,2]])
print(data.loc['Utah'])
print(data.iloc[2])
print(data.loc[['Ohio','Utah'],['two','four']])
print(data.iloc[[0,2],[1,3]])
# 索引的功能还可以用于切片
print(data.loc[:'Utah','two'])
print(data.iloc[:,:3][data.three > 5])
# 算术合数据对齐
# 对象相加时，如果存在某个索引对不相同，
# 则返回结果的索引将是索引对的并集
s1 = pd.Series([7.3, -2.5, 3.4, 1.5],
               index = ['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4.1, 3.1],
               index = ['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
print(s1 + s2)
df1 = pd.DataFrame(np.arange(9).reshape((3,3)),
                   index=['Ohio','Texas','Colorado'],
                   columns=list('bcd'))
df2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                   index=['Utah','Ohio','Texas','Oregon'],
                   columns=list('bde'))
print(df1)
print(df2)
print(df1 + df2)
# 使用填充值的算法方法
df1 = pd.DataFrame(data = np.arange(12.).reshape((3,4)),
                   columns = list('abcd'))
df2 = pd.DataFrame(data = np.arange(20.0).reshape((4,5)),
                   columns=list('abcde'))
print(df1)
print(df2)
print(df1 + df2)
# 加法
add = df1.add(df2,fill_value=0)
print(add)
# 减法
sub = df1.sub(df2, fill_value = 0)
print(sub)
# 除法
div = df1.div(df2, fill_value = 0)
print(div)
# 整除
floordiv = df1.floordiv(df2, fill_value = 0)
print(floordiv)
# 乘法
mul = df1.mul(df2, fill_value = 0)
print(mul)
# 幂次方
pow = df1.pow(df2, fill_value = 0)
print(pow)
# DataFrame和Series间的操作
arr = np.arange(12).reshape((3,4))
print(arr)
print(arr - arr[0])
# 以上是所谓的广播机制
frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                     columns=list('bde'),
                     index = ['Utah','Ohio','Texas','Oregon'])
series = frame.iloc[0,]
print(frame)
print(series)
# 默认情况下，DataFrame和Series的数学操作中会将Series
# 的索引和DataFrame的列进行匹配，并广播到各行
print(frame - series)
print(frame)
# 如果一个索引值不在DataFrame中，也不在Series中，
# 则对象会重建索引并形成关联
series2 = pd.Series(range(3),index=['b','e','f'])
print(series2)
print(frame + series2)
series3 = frame['d']
print(series3)
# 如果想要改为在列上进行广播，在行上匹配，
# 你必须使用算术方法中的一种
# axis用于匹配轴的
print(frame.sub(series3, axis='index'))